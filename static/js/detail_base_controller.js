$.ajaxSetup({
    async: false
});

var loadData = function() {
  $.getJSON(item_url,
    {
      id: id
    },
    renderData);
};

var renderData = function(data) {
  $('#item')
    .append($("<img/>")
      .attr("src", MEDIA_URL + data.img)
      .attr("class", "itemPic am-img-thumbnail"))
    .append($("<div></div>")
      .attr("class", "itemDetail am-thumbnail-caption"));

  $.each(data.key, function(index, value) {
    $('.itemDetail').append(
      $("<div></div>")
        .attr("class", "tableHead am-u-sm-4")
        .append(value + "：")
    );
    $('.itemDetail').append(
      $("<div></div>")
        .attr("class", "am-u-sm-8")
        .append(data[value])
    );
    $('.itemDetail').append($('<br><hr>'));
  })
};

var init = function() {
  loadData();
};