var CategorySelector = React.createClass({
  loadCategoriesFromServer: function() {
    $.ajax({
      url: this.props.url,
      data: {},
      dataType: 'json',
      cache: false,
      success: function(data) {
        this.setState({
          categories: data.data
        });
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },

  getInitialState: function() {
    return {
      categories: []
    };
  },

  componentDidMount: function() {
    this.loadCategoriesFromServer();
  },

  render: function() {
    var categoryNodes = this.state.categories.map(function(cat) {
      return (
        React.createElement('option', {value: cat.pk}, cat.name)
      )
    }.bind(this));
    return (
      <select id="category-selector" onChange={this.props.switchCategory}>
        {categoryNodes}
      </select>
    )
  }
});

var LocationSelector = React.createClass({
  loadLocationsFromServer: function() {
    $.ajax({
      url: this.props.url,
      data: {},
      dataType: 'json',
      cache: false,
      success: function(data) {
        this.setState({
          locations: data.data
        });
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },

  getInitialState: function() {
    return {
      locations: []
    };
  },

  componentDidMount: function() {
    this.loadLocationsFromServer();
  },

  render: function() {
    var locationNodes = this.state.locations.map(function(loc) {
      return (
        React.createElement('option', {value: loc.pk}, loc.name)
      )
    }.bind(this));
    return (
      <select id="location-selector" onChange={this.props.switchLocation}>
        {locationNodes}
      </select>
    )
  }
});

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

var PageSelector = React.createClass({
  render: function () {
    if (this.props.data.page > 1 && !this.props.data.end_of_list) {
      return (
        React.createElement('div', {},
          React.createElement('a', {onClick: this.props.prevPage},
            '上一页'
          ),
          React.createElement('a', {onClick: this.props.nextPage},
            '下一页'
          )
        )
      );
    }
    else if (this.props.data.page > 1 && this.props.data.end_of_list) {
      return (
        React.createElement('div', {},
          React.createElement('a', {onClick: this.props.prevPage},
            '上一页'
          )
        )
      );
    }
    else if (this.props.data.page == 1 && !this.props.data.end_of_list) {
      return (
        React.createElement('div', {},
          React.createElement('a', {onClick: this.props.nextPage},
            '下一页'
          )
        )
      );
    }
    else {
      return (
        React.createElement('div', {id: 'page-selector'})
      )
    }
  }
});

var FoundBox = React.createClass({
  loadFoundsFromServer: function(page=1, category=0, location=0) {
    $.ajax({
      url: this.props.url,
      data: {
        page: page,
        category: category,
        location: location
      },
      dataType: 'json',
      cache: false,
      success: function(data) {
        this.setState({
          founds: data.founds,
          page: data.page,
          category: data.category,
          location: data.location,
          end_of_list: data.end_of_list
        });
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },

  getInitialState: function() {
    return {
      founds: [],
      page: 1,
      category: 0,
      location: 0,
      end_of_list: false
    };
  },

  componentDidMount: function() {
    this.loadFoundsFromServer();gi
  },

  switchCategory: function() {
    var i = document.getElementById("category-selector");
    var v = i.options[i.selectedIndex].value;
    this.loadFoundsFromServer(1, v, this.state.location);
  },

  switchLocation: function() {
    var i = document.getElementById("location-selector");
    var v = i.options[i.selectedIndex].value;
    this.loadFoundsFromServer(1, this.state.category, v);
  },

  prevPage: function() {
    --this.state.page;
    this.loadFoundsFromServer(this.state.page, this.state.category, this.state.location);
  },

  nextPage: function() {
    ++this.state.page;
    this.loadFoundsFromServer(this.state.page, this.state.category, this.state.location);
  },

  render: function() {
    return (
      <div className="foundBox">
        <CategorySelector url="api/getCategories" switchCategory={this.switchCategory} />
        <LocationSelector url="api/getLocations" switchLocation={this.switchLocation} />
        <FoundList data={this.state.founds} />
        <PageSelector data={{
          page: this.state.page,
          end_of_list: this.state.end_of_list
        }} prevPage={this.prevPage} nextPage={this.nextPage} />
      </div>
    );
  }
});

ReactDOM.render(
  <FoundBox  url="api/getFoundItems" />,
  document.getElementById('content')
);
