# Panel de análisis de vehículos usados – Sprint 7

Este proyecto permite visualizar datos de vehículos usados mediante filtros interactivos y gráficos con Streamlit y Plotly.

## Funcionalidades

- Filtro por año del modelo (slider)
- Filtro doble: fabricante y variable de análisis (selectbox)
- Histograma con porcentajes (`histnorm='percent'`)
- Gráfico de dispersión opcional (checkbox)
- Comentarios técnicos integrados con `st.markdown`

## Requisitos

- Python 3.x
- Streamlit
- Pandas
- Plotly

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
streamlit run app.py
```

## Despliegue

Este proyecto puede desplegarse en [Render](https://render.com) conectando el repositorio y usando:

- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `streamlit run app.py`
