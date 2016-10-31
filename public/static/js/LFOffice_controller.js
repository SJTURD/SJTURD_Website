var content = NaN;
var page = NaN;
var item_per_page = 100;


var keyword = $('input[id=searchBox]').val();

$.ajaxSetup({
    async: false
});

var loadData = function() {
  var cur_content = [];
  cur_content = content;

  if (cur_content.length == 0) page = 1;

  var req = {
    data: cur_content,
    begin_of_list: (page == 1),
    end_of_list: (page * item_per_page >= cur_content.length),
  }

  renderData(req);
};

var renderData = function(data) {
  data=[{"model": "main.LFOffice", "pk": 1, "fields": {"contact": "null", "detail": "三餐一楼交大吃吃值班处", "name": "三餐"}}, {"model": "main.LFOffice", "pk": 2, "fields": {"contact": "null", "detail": "四餐一楼交大吃吃值班处", "name": "四餐"}}, {"model": "main.LFOffice", "pk": 3, "fields": {"contact": "null", "detail": "五餐二楼学生餐厅门口", "name": "五餐"}}, {"model": "main.LFOffice", "pk": 4, "fields": {"contact": "null", "detail": "哈乐餐厅刷卡处", "name": "哈乐餐厅"}}, {"model": "main.LFOffice", "pk": 5, "fields": {"contact": "021-54743923", "detail": "东上院二楼小卖部（管理室）", "name": "东上院"}}, {"model": "main.LFOffice", "pk": 6, "fields": {"contact": "18721443760", "detail": "东中院东中2-203旁管理室", "name": "东中院"}}, {"model": "main.LFOffice", "pk": 7, "fields": {"contact": "null", "detail": "东下院东下一楼小卖部（管理室）", "name": "东下院"}}, {"model": "main.LFOffice", "pk": 8, "fields": {"contact": "null", "detail": "光彪楼一楼光彪楼一楼楼梯处", "name": "光彪楼一楼"}}, {"model": "main.LFOffice", "pk": 9, "fields": {"contact": "null", "detail": "光标楼二楼二楼大厅值班处", "name": "光标楼二楼"}}, {"model": "main.LFOffice", "pk": 10, "fields": {"contact": "021-54742441", "detail": "下院下院311", "name": "下院"}}, {"model": "main.LFOffice", "pk": 11, "fields": {"contact": "021-54742441", "detail": "中院下院311", "name": "中院"}}, {"model": "main.LFOffice", "pk": 12, "fields": {"contact": "021-54742441", "detail": "上院下院311", "name": "上院"}}, {"model": "main.LFOffice", "pk": 13, "fields": {"contact": "18930902323", "detail": "致远游泳馆致远游泳馆前台", "name": "致远游泳馆"}}, {"model": "main.LFOffice", "pk": 14, "fields": {"contact": "null", "detail": "逸夫楼一楼值班处", "name": "逸夫楼"}}, {"model": "main.LFOffice", "pk": 15, "fields": {"contact": "null", "detail": "哈乐餐厅刷卡处", "name": "哈乐餐厅"}}, {"model": "main.LFOffice", "pk": 16, "fields": {"contact": "null", "detail": "南体体育场内场馆102", "name": "南体"}}, {"model": "main.LFOffice", "pk": 17, "fields": {"contact": "null", "detail": "一餐浴室一楼小房间", "name": "一餐浴室"}}, {"model": "main.LFOffice", "pk": 18, "fields": {"contact": "18217209329", "detail": "爱心屋商业街爱心屋内", "name": "爱心屋"}}, {"model": "main.LFOffice", "pk": 19, "fields": {"contact": "15821883878", "detail": "思源门门口爱心亭亭内", "name": "思源门门口爱心亭"}}, {"model": "main.LFOffice", "pk": 20, "fields": {"contact": "18217191627", "detail": "保卫处老行政楼二楼", "name": "保卫处"}}, {"model": "main.LFOffice", "pk": 21, "fields": {"contact": "null", "detail": "包玉刚图书馆一楼值班处", "name": "包玉刚图书馆"}}, {"model": "main.LFOffice", "pk": 22, "fields": {"contact": "null", "detail": "包玉刚图书馆一楼保安台", "name": "包玉刚图书馆"}}, {"model": "main.LFOffice", "pk": 23, "fields": {"contact": "null", "detail": "新图保安室", "name": "新图"}}, {"model": "main.LFOffice", "pk": 24, "fields": {"contact": "null", "detail": "霍英东体育馆一楼物业处", "name": "霍英东体育馆"}}, {"model": "main.LFOffice", "pk": 25, "fields": {"contact": "null", "detail": "陈瑞球楼一楼正门物业室", "name": "陈瑞球楼"}}, {"model": "main.LFOffice", "pk": 26, "fields": {"contact": "null", "detail": "二餐外现金充值处二餐浴室旁", "name": "二餐外现金充值处"}}, {"model": "main.LFOffice", "pk": 27, "fields": {"contact": "null", "detail": "一餐外现金充值处一餐浴室附近", "name": "一餐外现金充值处"}}, {"model": "main.LFOffice", "pk": 10001, "fields": {"contact": "null", "detail": "留在原地", "name": "留在原地"}}, {"model": "main.LFOffice", "pk": 10002, "fields": {"contact": "null", "detail": "自持", "name": "自持"}}];
  $('#card-table table tbody').empty();
  $.each(data, function(index, value) {
    $('#card-table table tbody').append(
      $("<tr></tr>")
        .attr("id", "card_" + value.pk)
        .append($("<td></td>")
          .append(value.fields.name))
        .append($("<td></td>")
          .append(value.fields.detail))
        .append($("<td></td>")
          .append(value.fields.contact))
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
}

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