

import pandas as pd
import streamlit as st
import plotly.express as px

# Cargar datos
car_data = pd.read_csv('data/vehicles_us_full.csv')
# car_data = pd.concat([car_data] * 20, ignore_index=True)
# st.write("Columnas disponibles:", car_data.columns.tolist())
# Tabla con scroll
st.header('🚗 Tabla de Vehículos con Scroll')
st.dataframe(car_data, height=400)

# Gráfica de barras: Condición vs Año del Modelo
st.header('📊 Gráfica de barras: Condición vs Año del Modelo')
fig_bar = px.bar(
    car_data.groupby(['condition', 'model_year']).size().reset_index(name='count'),
    x='model_year', y='count', color='condition', barmode='group'
)
st.plotly_chart(fig_bar, use_container_width=True)

# Histograma individual con checkbox
st.header('📊 Histograma de Odómetro por Condición')

if st.checkbox('Mostrar histograma detallado'):
    fig_hist = px.histogram(
        car_data,
        x='odometer',
        color='condition',
        histnorm='percent',
        barmode='overlay',
        nbins=30,
        opacity=0.7
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# Segundo histograma comparativo con separador de pestañas
st.header('📊 Comparador de histogramas superpuestos por fabricante')

# Lista de fabricantes únicos
fabricantes = car_data['brand'].dropna().unique()

# Selección de los dos fabricantes
fab1 = st.selectbox('Selecciona el primer fabricante', fabricantes)
fab2 = st.selectbox('Selecciona el segundo fabricante', fabricantes)

# Checkbox para normalizar
normalize = st.checkbox("Normalizar histograma", value=True)

# Filtrar datos
filtered = car_data[car_data['brand'].isin([fab1, fab2])]

# Crear histograma superpuesto
fig = px.histogram(
    filtered,
    x='odometer',
    color='brand',
    barmode='overlay',  # Para superponer las barras
    histnorm='percent' if normalize else None
)

# Mostrar gráfico
st.plotly_chart(fig, use_container_width=True)

# Comentario final
st.markdown('---')
st.write('Aplicación creada como parte del Sprint 7 – TripleTen')
