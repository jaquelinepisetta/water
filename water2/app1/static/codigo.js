window.onload = function (){

  var mapa = L.map("meumapa",{
    measureControl:true,
    center: [-25.5, -49.25],
    zoom: 11,
    zoomSnap: 0.5,
    zoomDelta: 0.5,
    minZoom: 4.5,
    maxZoom: 18
  })

  var OpenStreetMap_BlackAndWhite = L.tileLayer('http://{s}.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png', {
	maxZoom: 18,
	attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
});

//6 - Popup com as coordenadas no click do usuario
	mapa.on("click", function(evento) {
    $("#formulario").show();
    document.getElementById('ponto').value = JSON.stringify( evento.latlng);
    // console.log(evento.latlng.toGeoJSON())
			var popup = L.popup()
			.setLatLng(evento)
			.setContent("<b>Você clicou em: </b><br />" + evento.latlng)
			.openOn(mapa);
});

var OpenStreetMap2 = L.tileLayer('http://{s}.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png', {
maxZoom: 18,
attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(mapa);

var osmnovo = L.tileLayer("http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png")


  //Zoom para a posiçao do usuário
  mapa.locate({
    setView: true,
    maxZoom: 18,
    timeout: 100000
  });

//adicionando o shape
L.geoJSON(bairros, {
  style: function(feicao){
    cores = ["#a6cee3", "#1f78b4", "#b2df8a", "#33a02c", "#fb9a99", "#e31a1c", "#fdbf6f", "#ff7f00", "#cab2d6", "#6a3d9a", "#ffff99", "#b15928"];
    return{
      weight: 0.2,
      color: "#000",
      fillColor: cores[feicao.properties.CD_REGIONA-1],
      fillOpacity: 0.5
    }
  },
  onEachFeature: function (feicao, camada){
    camada.bindTooltip(feicao.properties.NOME)
  }
}).addTo(mapa);

//adicionando o shape
L.geoJSON(hidrol, {
  style: function(feicao){
      return{
      weight: 0.5,
      color: "#000",
      fillOpacity: 1
    }
  },
  }).addTo(mapa);

var miniMap = new L.Control.MiniMap(OpenStreetMap_BlackAndWhite).addTo(mapa);


//Mapas base
var bases = {
"Base Open Street Map": osmnovo,
"OSM": OpenStreetMap2
}

}
