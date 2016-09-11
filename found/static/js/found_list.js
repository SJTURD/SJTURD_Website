var FoundList = React.createClass({
  render: function() {
    var foundNodes = this.props.data.map(function(found) {
      return (
        <div>
          <img src={MEDIA_URL + found.fields.picture} />
          <p>{found.fields.category}</p>
        </div>
      );
    });
    return (
      <div className="foundList">
        {foundNodes}
      </div>
    );
  }
});

var FoundBox = React.createClass({
  loadDefaultFoundsFromServer: function() {
    $.ajax({
      url: this.props.url,
      data: {
        page: 1,
        category: 0,
        location: 0
      },
      dataType: 'json',
      cache: false,
      success: function(data) {
        this.setState({data: data});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },

  getInitialState: function() {
    return {data: []};
  },

  componentDidMount: function() {
    this.loadDefaultFoundsFromServer();
  },

  render: function() {
    return (
      <div className="foundBox">
        <FoundList data={this.state.data} />
      </div>
    );
  }
});

ReactDOM.render(
  <FoundBox  url="api/getFoundItems" />,
  document.getElementById('content')
);
