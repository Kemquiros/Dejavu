function select(ico){
  $("#ico").val(ico.getAttribute('id'));
  $("#img-ico").attr('src',ico.getAttribute('src'));
  $(".collapse").collapse('toggle');
}

function cargarIco(){
  var ruta = 'static/img/ico/';
  var iconoAleatorio = Math.floor((Math.random() * 789) + 1);
  $("#img-ico").attr('src',ruta+iconoAleatorio.toString()+'.png');
  $("#ico").val(iconoAleatorio);
  $("#collapseIco .card").empty() ;
  
  var contador = 1;
  for(i=0;i<263;i++){
    var contenedor = $('<div>');
    contenedor.addClass('row');
    $("#collapseIco .card").append(contenedor);
    for(j=0;j<3;j++){
      var fila = $('<div>');
      fila.addClass('col-lg-4');
      
      //Nuevo icono
      var nuevoIco = $('<img>');
      nuevoIco.addClass('img-ico-card');
      nuevoIco.attr('src',ruta+contador.toString()+'.png');
      nuevoIco.attr('onClick','select(this)');
      nuevoIco.attr('id',contador.toString());
      
      contenedor.append(fila);
      fila.append(nuevoIco);   
      contador++;
    }

  }

}
