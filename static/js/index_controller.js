var selector1_val = NaN;
var selector2_val = NaN;
var selector3_val = NaN;
var selector4_val = NaN;

$.ajaxSetup({
    async: false
});

var init = function() {

  var selector1_init = function(data) {
    selector1_val = data.default;

    $("#selector1").append(
      $("<option></option>")
        .attr("value", -1)
        .text('校园卡')
    );

    $.each(data.data, function(key, value) {
      $("#selector1").append(
        $("<option></option>")
          .attr("value", value.pk)
          .text(value.name)
      );
    });

    $('#selector1 option[value="' + selector1_val + '"]').attr('selected', 'selected');
  };

  $.getJSON(selector1_init_url, selector1_init);

  var selector2_init = function(data) {
    selector2_val = data.default;
    $.each(data.data, function(key, value) {
      $("#selector2").append(
        $("<option></option>")
          .attr("value", value.pk)
          .text(value.name)
      );
    });

    $('#selector2 option[value="' + selector2_val + '"]').attr('selected', 'selected');
  };

  $.getJSON(selector2_init_url, selector2_init);

  var selector3_init = function(data) {
    selector3_val = data.default;


    $.each(data.data, function(key, value) {
      $("#selector3").append(
        $("<option></option>")
          .attr("value", value.pk)
          .text(value.name)
      );
    });

    $('#selector3 option[value="' + selector3_val + '"]').attr('selected', 'selected');
  };

  $.getJSON(selector3_init_url, selector3_init);


    var selector4_init = function(data) {
    selector4_val = data.default;


    $.each(data.data, function(key, value) {
      $("#selector4").append(
        $("<option></option>")
          .attr("value", value.pk)
          .text(value.name)
      );
    });

    $('#selector4 option[value="' + selector4_val + '"]').attr('selected', 'selected');
  };

  $.getJSON(selector4_init_url, selector4_init);


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


var selector1 = function() {
  selector1_val = $("#selector1").val();
};

var selector2 = function() {
  selector2_val = $("#selector2").val();
};

var selector3 = function() {
  selector3_val = $("#selector1").val();
};

var selector4 = function() {
  selector4_val = $("#selector2").val();
};