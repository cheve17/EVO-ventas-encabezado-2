
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("📊 Dashboard Interactivo de Ventas Comex")

archivo_excel = "KPIs_Ventas_Comex.xlsx"
df_dict = pd.read_excel(archivo_excel, sheet_name=None)

kpi_seleccionado = st.sidebar.selectbox("Selecciona una hoja/KPI", list(df_dict.keys()))

df_kpi = df_dict[kpi_seleccionado]

# Aquí adaptas el gráfico según tus columnas reales
fig = px.line(df_kpi, x=df_kpi.columns[0], y=df_kpi.columns[1:], title=f"{kpi_seleccionado}")
st.plotly_chart(fig, use_container_width=True)
