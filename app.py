# Importando o streamlit, o Folium e o streamlit-folium
import streamlit as st
import folium
from streamlit_folium import folium_static

# Criando o objeto Map com a localização e o zoom de Brasília
m = folium.Map(location=[-15.793889, -47.882778], zoom_start=11)

# Criando um elemento HTML para mostrar as coordenadas do mouse
coordDIV = """
<div id='coordDIV' style='position: fixed; bottom: 50px; left: 10px; z-index: 9999; background-color: white; padding: 5px; border: 1px solid black;'>
Clique no mapa para ver as coordenadas
</div>
"""

# Adicionando o elemento HTML ao mapa
m.get_root().html.add_child(folium.Element(coordDIV))

# Criando uma função JavaScript para atualizar o elemento HTML com as coordenadas do clique
update_coordDIV = """
function updateCoordDIV(e) {
  var coordDIV = document.getElementById('coordDIV');
  var lat = e.latlng.lat.toFixed(6);
  var lng = e.latlng.lng.toFixed(6);
  coordDIV.innerHTML = 'Latitude: ' + lat + '<br>Longitude: ' + lng;
}
"""

# Adicionando a função JavaScript ao mapa
m.get_root().header.add_child(folium.Element('<script type="text/javascript">{}</script>'.format(update_coordDIV)))

# Criando um evento de clique no mapa que chama a função JavaScript
m.add_child(folium.LatLngPopup())

# Criando uma função Python para criar um marcador com o Folium a partir das coordenadas do clique
def add_marker(e):
  folium.Marker(location=[e.latlng.lat, e.latlng.lng], popup='Marcador').add_to(m)

# Adicionando um evento de clique no mapa que chama a função Python
m.add_child(folium.ClickForMarker(popup='Marcador'))

# Exibindo o mapa com o streamlit-folium
folium_static(m)
