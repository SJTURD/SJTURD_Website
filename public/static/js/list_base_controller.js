var selector1_val = NaN;
var selector2_val = NaN;
var page = NaN;
var end_of_list = false;

var getUrlParameter = function getUrlParameter(sParam) {
  var sPageURL = decodeURIComponent(window.location.search.substring(1)),
    sURLVariables = sPageURL.split('&'),
    sParameterName,
    i;

  for (i = 0; i < sURLVariables.length; i++) {
    sParameterName = sURLVariables[i].split('=');

    if (sParameterName[0] === sParam) {
      return sParameterName[1] === undefined ? true : sParameterName[1];
    }
  }
};

$.ajaxSetup({
    async: false
});

var loadData = function() {
  $.getJSON(items_url,
    {
      page: page,
      selector1_val: selector1_val,
      selector2_val: selector2_val
    },
    renderData);
};

var renderData = function(data) {
  $('#item-list ul').empty();
  $.each(data.data, function(index, value) {
    $('#item-list ul').append(
      $("<li></li>")
        .attr("onclick", "window.location.href='" + value.url + "'")
        .attr("class", "item am-thumbnail")
        .append($("<img/>")
          .attr("src", MEDIA_URL + value.img)
          .attr("class", "itemPic am-img-thumbnail"))
        .append($("<div></div>")
          .attr("class", "itemDetail am-thumbnail-caption")
          .append($("<div></div>")
            .attr("class", "left_field am-u-sm-8")
            .append(value.left_field))
          .append($("<div></div>")
            .attr("class", "right_field am-u-sm-4")
            .append(value.right_field))
          .append($("<div></div>")
            .attr("class", "bottom_field am-u-sm-12")
            .append(value.bottom_field)
          )
        )
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

  var selector1_init = function(data) {
    selector1_val = data.default;
    tmp = getUrlParameter("selector1");

    var flag = false;
    $.each(data.data, function(key, value) {
      $("#selector1").append(
        $("<option></option>")
          .attr("value", value.pk)
          .text(value.name)
      );
      if (value.pk == tmp) selector1_val = tmp;
    });

    $('#selector1 option[value="' + selector1_val + '"]').attr('selected', 'selected');
  };

  $.getJSON(selector1_init_url, selector1_init);

  var selector2_init = function(data) {
    selector2_val = data.default;
    tmp = getUrlParameter("selector2");
    $.each(data.data, function(key, value) {
      $("#selector2").append(
        $("<option></option>")
          .attr("value", value.pk)
          .text(value.name)
      );
      if (value.pk == tmp) selector2_val = tmp;
    });

    $('#selector2 option[value="' + selector2_val + '"]').attr('selected', 'selected');
  };

  $.getJSON(selector2_init_url, selector2_init);

  loadData();

  var selectorCSS = function() {
    $('select').each(function () {
      var $this = $(this), numberOfOptions = $(this).children('option').length;

      $this.addClass('select-hidden');
      $this.wrap('<div class="select"></div>');
      $this.after('<div class="select-styled"></div>');

      var $styledSelect = $this.next('div.select-styled');
      $styledSelect.text($this.children('option[selected=selected]').text());

      var $list = $('<ul />', {
        'class': 'select-options'
      }).insertAfter($styledSelect);

      for (var i = 0; i < numberOfOptions; i++) {
        $('<li />', {
          text: $this.children('option').eq(i).text(),
          rel: $this.children('option').eq(i).val()
        }).appendTo($list);
      }

      var $listItems = $list.children('li');


      $styledSelect.click(function (e) {
        if ($('.select-options').is(':visible')) {
          e.stopPropagation();
          $styledSelect.text($(this).text()).removeClass('active');
          $this.val($(this).attr('rel'));

          $list.hide();
          //console.log($this.val());

        } else {
          e.stopPropagation();
          $('div.select-styled.active').each(function () {
            $(this).removeClass('active').next('ul.select-options').hide();
          });
          $(this).toggleClass('active').next('ul.select-options').toggle();
        }//end if
      });

      $listItems.click(function (e) {
        e.stopPropagation();
        $styledSelect.text($(this).text()).removeClass('active');
        $this.val($(this).attr('rel'));
        $list.hide();
        var selectDiv = $(this).parents()[1];
        $(selectDiv).children("select").children().removeAttr('selected');
        $(selectDiv).children("select").children('option[value="' + $(this)
            .attr('rel') + '"]').attr('selected', 'selected');
        $(selectDiv).children("select")[0].onchange();
      });

      $(document).click(function () {
        $styledSelect.removeClass('active');
        $list.hide();
      });
    });
  };

  selectorCSS();
};

var prevPage = function() {
  --page;
  loadData();
};

var nextPage = function() {
  ++page;
  loadData();
};

var selector1 = function() {
  selector1_val = $("#selector1").val();
  loadData();
};

var selector2 = function() {
  selector2_val = $("#selector2").val();
  loadData();
};