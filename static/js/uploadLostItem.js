var Date = React.createClass({
  getInitialState: function() {
    return {appreciate: true};
  },
  handleClick: function(event) {
    this.setState({appreciate: !this.state.appreciate});
  },
  render: function() {
    var type1 = this.state.appreciate ? 'open1':'close1';
    var type2 = this.state.appreciate ? 'open2':'close2';
    return (
      <div class="am-g" id="appreciation">
        <div class="am-g" id="willing">
          <div class="am-u-sm-8">
             是否愿意感谢捡到您宝贝的同学？
            </div>
            <div class="am-u-sm-4">
              <div id="div1" class="{type1}" onClick={this.handleClick}>
                <div id="div2" class="{type2}"></div>
              </div>
            </div>
        </div>
      </div>
    );
  }
});


ReactDOM.render(
  <Date />,
  document.getElementById('appreciation')
);