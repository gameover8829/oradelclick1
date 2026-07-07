import streamlit as st
import pandas as pd
import urllib.parse

st.set_page_config(page_title="Ora del Click - Vendedores", layout="wide")
st.title("⚡ Ora del Click: Panel de Ventas")

# 1. Cargar datos (Conectado a tu Google Sheet publicado como CSV)
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQhKk4DCT5uIc9cWkxGFBBc-cMn14ATRDcKavNJPEfi2d3YYFXM1iLS92ujxoxVacgHrkl6RQUGPxH6/pub?output=csv"
df = pd.read_csv(SHEET_URL)

# 2. Tabs para organizar
tab1, tab2 = st.tabs(["🛒 Catálogo de Ofertas", "➕ Agregar Nueva Oferta"])

with tab1:
    st.subheader("Ofertas Activas")
    for _, row in df.iterrows():
        with st.container(border=True):
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(row['URL_Imagen'], use_container_width=True)
            with col2:
                st.markdown(f"### {row['Producto']}")
                st.write(f"**Precio:** {row['Precio_Oferta']} (Normal: {row['Precio_Original']})")
                
                # Generar mensaje de WhatsApp profesional
                texto = f"🔥 ¡Aprovecha este ofertón! {row['Producto']} por solo {row['Precio_Oferta']}. ¡Cómpralo aquí antes de que se agote!: {row['Link_ML_Acortado']}"
                wa_link = f"https://wa.me/?text={urllib.parse.quote(texto)}"
                
                st.link_button("📲 Enviar por WhatsApp", wa_link, use_container_width=True)

with tab2:
    st.info("Usa este formulario para enviar una nueva oferta al catálogo.")
    with st.form("nueva_oferta"):
        prod = st.text_input("Nombre del Producto")
        p_oferta = st.text_input("Precio de Oferta")
        link = st.text_input("Link de Mercado Libre (Acortado)")
        img = st.text_input("URL de la Imagen")
        submit = st.form_submit_button("Enviar a revisión")
        
        if submit:
            st.success("¡Oferta enviada! Se mostrará en el catálogo en breve.")
            # Aquí podrías conectar a un script de Google Apps para auto-guardar
