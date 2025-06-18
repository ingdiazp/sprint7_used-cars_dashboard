
import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
df = pd.read_csv("vehicles_us.csv")

# Título de la aplicación
st.title("Dashboard de Vehículos Usados")

# Selectbox para elegir marca (brand)
marcas = df["brand"].unique()
marca_seleccionada = st.selectbox("Selecciona una marca:", marcas)

# Filtrar los datos
df_filtrado = df[df["brand"] == marca_seleccionada]

# Calcular métricas
total_modelos = df_filtrado["model"].nunique()
año_promedio = df_filtrado["year"].mean()
precio_promedio = df_filtrado["price"].mean()

# Mostrar métricas
st.metric("Modelos disponibles", total_modelos)
st.metric("Año promedio", round(año_promedio, 1))
st.metric("Precio promedio (USD)", f"{round(precio_promedio):,}")

# Checkbox para mostrar tabla filtrada
if st.checkbox("Mostrar datos filtrados"):
    st.dataframe(df_filtrado)

# Histograma del odómetro
st.subheader("Distribución del odómetro")
fig = px.histogram(df_filtrado, x='odometer', nbins=20, title='Kilometraje por marca seleccionada')
st.plotly_chart(fig, use_container_width=True)
