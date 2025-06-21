
import pandas as pd
import streamlit as st
import plotly.express as px

# Cargar datos
car_data = pd.read_csv('data/vehicles_us_full.csv')

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
st.header('📈 Histograma: Odómetro')
if st.checkbox('Mostrar histograma de odómetro'):
    fig_hist = px.histogram(car_data, x='odometer', histnorm='percent')
    st.plotly_chart(fig_hist, use_container_width=True)

# Segundo histograma comparativo con separador de pestañas
st.header('📊 Comparador de histogramas por fabricante')
fabricantes = car_data['manufacturer'].dropna().unique()
fab1 = st.selectbox('Selecciona el primer fabricante', fabricantes)
fab2 = st.selectbox('Selecciona el segundo fabricante', fabricantes, index=1)

filtered1 = car_data[car_data['manufacturer'] == fab1]
filtered2 = car_data[car_data['manufacturer'] == fab2]

tab1, tab2 = st.tabs([fab1, fab2])

with tab1:
    st.subheader(f'Histograma para {fab1}')
    fig1 = px.histogram(filtered1, x='odometer', histnorm='percent')
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    st.subheader(f'Histograma para {fab2}')
    fig2 = px.histogram(filtered2, x='odometer', histnorm='percent')
    st.plotly_chart(fig2, use_container_width=True)

# Comentario final
st.markdown('---')
st.write('Aplicación creada como parte del Sprint 7 – TripleTen')
