var content = NaN;
var page = NaN;
var item_per_page = 100;


var keyword = $('input[id=searchBox]').val();

$.ajaxSetup({
    async: false
});

var loadData = function() {
  var cur_content = [];
  if (keyword) {
    $.each(content, function(index, value) {
      if (value.student_id.search(keyword) != -1 || value.name.search(keyword) != -1) cur_content.push(value);
    });
  }
  else {
    cur_content = content;
  }

  if (cur_content.length == 0) page = 1;

  var req = {
    data: cur_content.slice(item_per_page * (page - 1), item_per_page * page),
    begin_of_list: (page == 1),
    end_of_list: (page * item_per_page >= cur_content.length),
  };

  renderData(req);
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

  var begin_of_list = data.begin_of_list;
  var end_of_list = data.end_of_list;

  if (begin_of_list) {
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

var init_content = function(data) {
  content = data.data;
  page = 1;
};

var init = function() {
  $.getJSON(items_url, init_content);
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

var changeKeyword = function() {
  keyword = $('input[id=searchBox]').val();
  page = 1;
  loadData();
};