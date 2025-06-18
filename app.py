import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
df = pd.read_csv("data/vehicles_us.csv")

# Título y descripción general
st.title("Panel de análisis de vehículos usados")
st.markdown("Esta app interactiva permite explorar datos de vehículos usados con filtros dinámicos y visualizaciones con Plotly.")

# Filtro por año de modelo
year_range = st.slider("Selecciona el rango de años del modelo:", int(df['model_year'].min()), int(df['model_year'].max()), (2010, 2015))
df_filtered = df[(df['model_year'] >= year_range[0]) & (df['model_year'] <= year_range[1])]

# Selectbox doble (fabricante y variable)
manufacturers = df['manufacturer'].dropna().unique()
variables = ['price', 'odometer', 'days_listed']
selected_manu = st.selectbox("Selecciona el fabricante:", manufacturers)
selected_var = st.selectbox("Selecciona la variable a analizar:", variables)

df_filtered = df_filtered[df_filtered['manufacturer'] == selected_manu]

# Histograma con histnorm='percent'
st.subheader("Distribución porcentual del valor seleccionado")
fig_hist = px.histogram(df_filtered, x=selected_var, histnorm='percent', nbins=30, title=f"Distribución porcentual de {selected_var}")
fig_hist.update_traces(marker_color='orange', hovertemplate="%{x}: %{y}%")
st.plotly_chart(fig_hist, use_container_width=True)

# Checkbox para mostrar gráfico de dispersión
if st.checkbox("Mostrar gráfico de dispersión (price vs. odometer)"):
    st.subheader("Relación entre precio y kilometraje")
    fig_scatter = px.scatter(df_filtered, x="odometer", y="price", color="condition",
                             hover_data=["model_year", "type"], title="Dispersión: Precio vs Kilometraje")
    st.plotly_chart(fig_scatter, use_container_width=True)

# Comentarios técnicos
st.markdown("""
### Notas técnicas:
- El histograma muestra porcentajes relativos (`histnorm='percent'`) para facilitar comparación.
- El gráfico de dispersión solo se muestra si se activa la opción correspondiente.
- Los datos están filtrados por rango de años y fabricante.
""")
