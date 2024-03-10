import streamlit as st
import folium
from streamlit_folium import folium_static

def main():
    st.title("Adicionar Marcador no Mapa")

    # Criando um mapa com o Folium
    m = folium.Map(location=[-15.793889, -47.882778], zoom_start=10)

    # Função para adicionar marcador no mapa
    def add_marker(lat, lon):
        folium.Marker([lat, lon], popup=f"Coordenadas: {lat}, {lon}").add_to(m)
        folium.CircleMarker([lat, lon], radius=5, color='blue', fill_color='blue').add_to(m)
        st.write("Marcador adicionado com sucesso!")

    # Streamlit
    col1, col2 = st.columns([3, 1])

    # Renderizando o mapa
    with col1:
        folium_static(m)

    # Botão para adicionar marcador
    with col2:
        st.write("Clique no mapa para adicionar um marcador")
        lat, lon = st.map("Mapa")

        if st.button("Adicionar Marcador"):
            add_marker(lat, lon)

if __name__ == "__main__":
    main()
