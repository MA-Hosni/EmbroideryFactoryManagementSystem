$(document).ready(function() {
  $(".menu > ul > li").click(function(e) {
    e.stopPropagation(); // Prevent click event from propagating to parent elements
    $(this).siblings().removeClass("active");
    $(this).toggleClass("active");
    $(this).find("ul").slideToggle();
    $(this).siblings().find("ul").slideUp();
    $(this).siblings().find("li").removeClass("active");
  });

  // When clicking outside the menu, slide up the "Users" menu and remove "active" class from all menu items
  $(document).click(function(e) {
    if (!$(e.target).closest(".menu > ul > li").length) {
      $(".menu > ul > li").removeClass("active");
      $(".menu > ul > li > ul").slideUp();
    }
  });

  // Prevent slide up when clicking on sub-menu items
  $(".menu > ul > li > ul").click(function(e) {
    e.stopPropagation(); // Prevent click event from propagating to parent elements
  });

  // Add "active" class to sub-menu items when clicked
  $(".menu > ul > li > ul > li").click(function(e) {
    e.stopPropagation();
    $(this).siblings().removeClass("active");
    $(this).toggleClass("active");
  });
  $("#permission-sub-menu").slideDown();

});




$(".menu-btn").click(function () {
  $(".sidebar").toggleClass("active");
});