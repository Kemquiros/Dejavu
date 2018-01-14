function getGames(){
  jQuery.get("/games-list", function(data, status){
      $("tbody").empty();      
      jQuery.each(data, function() {       
       var row = $('<tr>');
        
       var c1 = $('<td>');
       var c2 = $('<td>');
       var c3 = $('<td>');
       var c4 = $('<td>');
       var c5 = $('<td>');
       var c6 = $('<td>');
       row.append(c1);
       row.append(c2);
       row.append(c3);
       row.append(c4);
       row.append(c5);
       row.append(c6);       
       c1.text(this['inicioPartida']);
       c2.text(this['creador']);
       c3.text(this['nombre']);
       c4.text(this['numeroJugadores']+" / "+this['numeroJugadoresMax']);
       c5.text(this['estado']);
       var formulario = $('<form>');
       c6.append(formulario);
       if(this['estado']=="pendiente" && this['numeroJugadores'] < this['numeroJugadoresMax']){
        formulario.attr('action','/join-player');
        formulario.attr('method','post');
        formulario.append($('<input>')
                         .attr('type','hidden')
                         .attr('id','partida')
                         .attr('name','partida')
                         .attr('value',this['nombre'])
                         );
        formulario.append($('<button>')
                          .attr('type','submit')
                          .addClass('btn btn-outline-success')
                          .text('Unirse')
                         );
       }else if(this['estado']=="activa"){
        formulario.append($('<button>')
                          .attr('type','submit')
                          .addClass('btn btn-outline-info')
                          .text('Ver')
                         );
       }               
        $("tbody").append(row);
      });
  });  
}
function initClock(){
  var reloj = setInterval(getGames, 1000);  
  $(window).on('hashchange', function(e){
    clearInterval(reloj);
  });
}