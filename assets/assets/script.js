
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
/*spacific tabs*/
function openreport(evt, reportlist) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(reportlist).style.display = "block";
  evt.currentTarget.className += " active";
}
/**/
/*navbar change color*/
$(function () {
  $(document).scroll(function () {
    var $nav = $(".navbar");
    $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
  });
});

/*dropdown setting*/