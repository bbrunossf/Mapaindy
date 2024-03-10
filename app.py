# Importando o streamlit, o Folium e o streamlit-folium
import streamlit as st
import folium
from streamlit_folium import folium_static

# Criando o objeto Map com a localização e o zoom de Brasília
m = folium.Map(location=[-15.793889, -47.882778], zoom_start=11)

# Criando uma caixa de texto para receber a coordenada do usuário
coord = st.text_input('Digite a coordenada do marcador (ex: [-15.7589665, -47.879422])', '[-15.7589665, -47.879422]', type='default')

# Criando um botão para adicionar o marcador
if st.button('Adicionar marcador'):
  # Tentando converter a entrada em uma lista de números
  try:
    coord = eval(coord)
    # Verificando se a entrada é uma lista de dois números
    if isinstance(coord, list) and len(coord) == 2 and all(isinstance(x, (int, float)) for x in coord):
      # Criando o objeto Marker com a coordenada, o popup e o ícone
      marker = folium.Marker(location=coord, popup='Marcador', icon=folium.Icon(color='red', icon='info-sign'))
      # Adicionando o marcador ao mapa
      marker.add_to(m)
      # Exibindo uma mensagem de sucesso
      st.success('Marcador adicionado com sucesso!')
    else:
      # Exibindo uma mensagem de erro
      st.error('Coordenada inválida. Digite uma lista de dois números separados por vírgula.')
  except:
    # Exibindo uma mensagem de erro
    st.error('Coordenada inválida. Digite uma lista de dois números separados por vírgula.')

# Exibindo o mapa com o streamlit-folium
folium_static(m)
