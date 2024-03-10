# Importando o streamlit, o Folium e o streamlit-folium
import streamlit as st
import folium
from streamlit_folium import folium_static

# Criando o objeto Map com a localização e o zoom de Brasília
m = folium.Map(location=[-15.793889, -47.882778], zoom_start=11)

# Criando uma variável global para armazenar a coordenada do clique
if 'coord' not in st.session_state:
  st.session_state.coord = None

# Criando uma função JavaScript para atualizar a variável e a caixa de texto com a coordenada do clique
update_coord = """
function updateCoord(e) {
  var coord = e.latlng.lat.toFixed(6) + ', ' + e.latlng.lng.toFixed(6);
  window.st.session_state.coord = coord;
  window.st.text_input('Coordenada do clique', coord, type='default', key='coord');
}
"""

# Adicionando a função JavaScript ao mapa
m.get_root().header.add_child(folium.Element('<script type="text/javascript">{}</script>'.format(update_coord)))

# Criando um evento de clique no mapa que chama a função JavaScript
m.add_child(folium.LatLngPopup())
st.text_input(value=update_coord)
# Criando um botão para adicionar o marcador
if st.button('Adicionar marcador'):
  # Tentando converter a entrada em uma lista de números
  try:
    coord = eval('[' + st.session_state.coord + ']')
    # Verificando se a entrada é uma lista de dois números
    if isinstance(coord, list) and len(coord) == 2 and all(isinstance(x, (int, float)) for x in coord):
      # Criando o objeto Marker com a coordenada, o popup e o ícone
      marker = folium.Marker(location=coord, popup='Marcador', icon=folium.Icon(color='red', icon='info-sign'))
      # Adicionando o marcador ao mapa
      marker.add_to(m)
      st.write(coord)
      # Exibindo uma mensagem de sucesso
      st.success('Marcador adicionado com sucesso!')
    else:
      # Exibindo uma mensagem de erro
      st.error('Coordenada inválida. Clique em um ponto do mapa.')
  except:
    # Exibindo uma mensagem de erro
    st.error('Coordenada inválida. Clique em um ponto do mapa.')
   
# Exibindo o mapa com o streamlit-folium
folium_static(m)
