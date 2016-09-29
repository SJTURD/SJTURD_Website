var LostList = React.createClass({
  render: function() {
    var lostNodes = this.props.data.map(function(lost) {
      return (
        <div>
          <img src={lost.picture} />
          <p>{lost.category}</p>
        </div>
      );
    });
    return (
      <div className="lostList">
        {lostNodes}
      </div>
    );
  }
});

var LostBox = React.createClass({
  loadDefaultLostsFromServer: function() {
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
    this.loadDefaultLostsFromServer();
  },

  render: function() {
    return (
      <div className="lostBox">
        <LostList data={this.state.data} />
      </div>
    );
  }
});

ReactDOM.render(
  <LostBox  url="api/getLostItems" />,
  document.getElementById('content')
);
