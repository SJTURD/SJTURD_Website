var page = NaN;
var end_of_list = false;

$.ajaxSetup({
    async: false
});

var loadData = function() {
  $.getJSON(items_url,
    {
      page: page
    },
    renderData);
};

var renderData = function(data) {
  $('#card-table table tbody').empty();
  $.each(data.data, function(index, value) {
    $('#card-table table tbody').append(
      $("<tr></tr>")
        .attr("id", "card_" + value.id)
        .append($("<td></td>")
          .append(value.student_id))
        .append($("<td></td>")
          .append(value.name))
        .append($("<td></td>")
          .append(value.lfoffice))
    )
  });

  page = data.page;
  end_of_list = data.end_of_list;

  if (page == 1) {
    $("#page-selector .am-pagination-prev").addClass("am-disabled")
  }
  else {
    $("#page-selector .am-pagination-prev").removeClass("am-disabled")
  }

  if (end_of_list) {
    $("#page-selector .am-pagination-next").addClass("am-disabled")
  }
  else {
    $("#page-selector .am-pagination-next").removeClass("am-disabled")
  }
};

var init = function() {
  page = 1;
  loadData();
};

var prevPage = function() {
  --page;
  loadData();
};

var nextPage = function() {
  ++page;
  loadData();
};

var highlightRows = function() {
  var keyword = $('input[id=searchBox]').val();

  $.each($("tbody tr"), function (index, value) {
    $(value).removeClass("am-active");
    if (keyword.length > 0 && ($(value).children().first().text().search(keyword) != -1 ||
      $(value).children().first().next().text().search(keyword) != -1))

      $(value).addClass("am-active");
  })
};