function getPlayers(){
  jQuery.get("/players", function(data, status){
      $("tbody").empty();
      jQuery.each(data, function() {
        var row = $('<tr>');
        
        var colico = $('<td>');
        var ico = $('<img>').attr('src','static/img/ico/'+this.icono+'.png');
        ico.addClass('img-ico');
        colico.append(ico);
        row.append(colico);
        
        var colnombre = $('<td>');
        colnombre.text(this.nombre);
        row.append(colnombre);
        
        var colraza = $('<td>');
        colraza.text(this.avatar.raza);
        row.append(colraza);
        
        $("tbody").append(row);
      });
  });  
}
function initClock(){
  var reloj = setInterval(getPlayers, 2000);  
  $(window).on('hashchange', function(e){
    clearInterval(reloj);
  });
}

