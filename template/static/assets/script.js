
  /*Slide recomend*/
  $('.slider-nav').slick({
    slidesToShow: 4,
    slidesToScroll: 2,
    dots: true,
    focusOnSelect: true,
    responsive: [
      {
          breakpoint: 1024,
          settings: {
              slidesToShow: 3,
              slidesToScroll: 2,
          }
      },
      {
          breakpoint: 800,
          settings: {
              slidesToShow: 2,
              slidesToScroll: 2
          }
      },
      {
          breakpoint: 480,
          settings: {
              slidesToShow: 1,
              slidesToScroll: 1
          }
      }

]
    
  });
/*End slide recomend*/
// navbar change color
$(function () {
  $(document).scroll(function () {
    var $nav = $(".navbar");
    $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
  });
});
// dashboard js
function openoptionreport(evt, reportlist) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent_report");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tabtab");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace("active", "");
  }
  if (document.getElementById(reportlist).style.display = "none"){
    document.getElementById(reportlist).style.display = "block";
  }else{
      document.getElementById(reportlist).style.display ="none"
  }
  evt.currentTarget.className += " active";
}

//Change button reply & comment movie
function editreply(id){
    var check = document.getElementById('replytext'+id)
    if (check.style.display == "inline-block"){
     $('#replytextedit'+id).prop('type', 'text');
     document.getElementById('replytext'+id).style.display="none";
     document.getElementById('replytextedit'+id).setAttribute("name", "replyedit")
     }else{
      $('#replytextedit'+id).prop('type', 'hidden');
     document.getElementById('replytext'+id).style.display="inline-block";
     }
}
function editcomment(id){
    var check = document.getElementById('commenttext'+id)
    if (check.style.display == "inline-block"){
     document.getElementById('commenttext'+id).style.display="none";
     document.getElementById('commenttextedit'+id).style.display="block";
     }else{
     document.getElementById('commenttextedit'+id).style.display="none";
     document.getElementById('commenttext'+id).style.display="inline-block";
     }
}
//comment webboard
function openeditcomment(id){
    comment = document.getElementById('editcomment'+id)
    commentold = document.getElementById('commentold'+id)
    if (comment.style.display == "none"){
        comment.style.display="block";
        $(commentold).hide();
        }else{
        comment.style.display="none";
        $(commentold).show();
        }
}
function openeditreply(id){
    reply = document.getElementById('editreply'+ id);
    replyold = document.getElementById('replyold'+id);
    if (reply.style.display == "none"){
        $(reply).show();
        $(replyold).hide();
    }else{
        $(replyold).show();
        $(reply).hide();
    }
}


//RATING STAR
/*!
 * jQuery lightweight plugin boilerplate
 * Original author: @ajpiano
 * Further changes, comments: @addyosmani
 * Licensed under the MIT license
 */

// the semi-colon before the function invocation is a safety
// net against concatenated scripts and/or other plugins
// that are not closed properly.
;(function ( $, window, document, undefined ) {

    // undefined is used here as the undefined global
    // variable in ECMAScript 3 and is mutable (i.e. it can
    // be changed by someone else). undefined isn't really
    // being passed in so we can ensure that its value is
    // truly undefined. In ES5, undefined can no longer be
    // modified.

    // window and document are passed through as local
    // variables rather than as globals, because this (slightly)
    // quickens the resolution process and can be more
    // efficiently minified (especially when both are
    // regularly referenced in your plugin).

    // Create the defaults once
    var pluginName = "ratingStar",
        defaults = {
          initialStar: 0,
          selectedClass: 'is-selected',
          hoverClass: 'is-hover',
          afterClick: null
        };

    // The actual plugin constructor
    function Plugin( element, options ) {
      this.$element = $(element);

      this.options = $.extend( {}, defaults, options) ;

      this._defaults = defaults;
      this._name = pluginName;

      this.init();
    }

    Plugin.prototype = {

        init: function() {
          var self = this;

          this.$starItems = this.$element.find('.c-rating-star__item');

          /* 1. Visualizing things on Hover - See next part for action on click */
          this.$starItems.on('mouseover', function(){
            self.onMouseOver(self, this);
          }).on('mouseout', function(){
            self.onMouseOut(self, this);
          });

          /* 2. Action to perform on click */
          this.$starItems.on('click', function(){
            self.onClick(self, this)
          });
        },

        onClick: function(context, jqContext) {
          var $this = $(jqContext);
          var $stars = context.$starItems;
          var onStar = parseInt($this.data('value'), 10); // The star currently selected

          // remove all active star
          $stars.removeClass('is-selected');

          for (i = 0; i < onStar; i++) {
            $stars.eq(i).addClass('is-selected');
          }

          var $selected = $this.parent().children('.is-selected').last();
          var ratingValue = parseInt($selected.data('value'), 10);

          if (context.options.afterClick) {
            context.options.afterClick(ratingValue, $selected);
          }
        },

        onMouseOver: function(context, jqContext) {
          // The star currently mouse on
          var currentStar = parseInt($(jqContext).data('value'), 10);

          // all start item
          var $stars = context.$starItems;

          // Now highlight all the stars that's not after the current hovered star
          for (i = 0; i <= currentStar; i++) {
            if (i < currentStar) {
              $stars.eq(i).addClass('is-hover');
            } else {
              $stars.eq(i).removeClass('is-hover');
            }
          }

          console.log('mouse over on: ',jqContext);
          console.log('current star: ', currentStar);

        },

        onMouseOut: function (context, jqContext) {
          for (i = 0; i <= context.$starItems.length; i++) {
            context.$starItems.eq(i).removeClass('is-hover');
          }
        }
    };

    // A really lightweight plugin wrapper around the constructor,
    // preventing against multiple instantiations
    $.fn[pluginName] = function ( options ) {
        return this.each(function () {
            if (!$.data(this, "plugin_" + pluginName)) {
                $.data(this, "plugin_" + pluginName,
                new Plugin( this, options ));
            }
        });
    };

})( jQuery, window, document );


$(document).ready(function(){

  $('#js-rating-star').ratingStar({
    afterClick: function (value, el) {
      $('.c-box').fadeIn(200);
      $('.c-box__body').html("<span>" + el.attr('title') + "</span>");
    }
  });

});

