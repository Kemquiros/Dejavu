function getPlayers(){
  jQuery.get("/players", function(data, status){
      $("tbody").empty();
      console.log(data);
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
  jQuery.get("/nro-players", function(data, status){
    //Actualiza el numero de jugadores
    $("#num").text(data["nro"]+" / "+data["nroMax"])
  });
}

function getState(){
  jQuery.get('/state', function(data, status){
   if(data['state'] == "pendiente"){
      getPlayers();
    }else if(data['state'] == "activa"){
      window.location.replace("/board");
    }else if(data['state'] == "terminada" || data['state'] == "no existe"){
      window.location.replace("/games");
    }
  });
}

function initClock(){
  var reloj = setInterval(getState, 2000);  
  $(window).on('hashchange', function(e){
    clearInterval(reloj);
  });
}

