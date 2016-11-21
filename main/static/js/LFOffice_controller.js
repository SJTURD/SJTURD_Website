var content = NaN;

$.ajaxSetup({
    async: false
});

var loadData = function() {
  req = content;
  renderData(req);
};

var renderData = function(data) {
  $('#lfoffice-table table tbody').empty();
  $.each(data, function(index, value) {
    if (parseInt(value.id) <= 10000) {
      $('#lfoffice-table table tbody').append(
        $("<tr></tr>")
          .attr("id", "lfoffice_" + value.id)
          .append($("<td></td>")
            .append(value.location))
          .append($("<td></td>")
            .append(value.remark))
      )
    }
  });
/*
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
*/
};

var init_content = function(data) {
  content = data.data;
};

var init = function() {
  $.getJSON(items_url, init_content);
  loadData();
};
/*
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
*/