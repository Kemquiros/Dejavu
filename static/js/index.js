
function select(ico){
  $("#ico").val(ico.getAttribute('id'));
  $("#img-ico").attr('src',ico.getAttribute('src'));
  $(".collapse").collapse('toggle');
}