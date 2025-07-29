import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import datetime
import os

db_path = "/Users/ignacioviera/Desktop/automatizacion-reporte-compras/reporte_compras.db"


conn = sqlite3.connect(db_path)

st.title("Dashboard de Compras")
st.markdown("Visualización interactiva de reportes de proveedores")

compras = pd.read_sql_query("SELECT * FROM compras", conn)

total_compras = compras["precio_total"].sum()

st.subheader("Resumen General")


col1, col2, col3 = st.columns(3)

with col1: 
    st.metric("Total Compras", f"${total_compras:,.2f}")

with col2: 
    st.metric("Compras Totales", len(compras))

with col3:
    st.metric("Cantidad de Proveedores", compras["proveedor"].nunique())



total_logiMax = compras[compras["proveedor"] == "LogiMax"]["precio_total"].sum()
total_megaTools = compras[compras["proveedor"] == "MegaTools"]["precio_total"].sum()
total_novaIndustrias = compras[compras["proveedor"] == "NovaIndustrias"]["precio_total"].sum()
total_techParts = compras[compras["proveedor"] == "TechParts"]["precio_total"].sum()

st.subheader("Total de compras por proveedor")

col1, col2, col3, col4 = st.columns(4)
with col1: 
    st.metric("Gasto Logi Max", f"${total_logiMax:,.2f}")

with col2: 
    st.metric("Gasto Mega Tools", f"${total_megaTools:,.2f}")

with col3: 
    st.metric("Gasto Nova Industrias", f"${total_novaIndustrias:,.2f}")

with col4: 
    st.metric("Gasto Tech Parts", f"${total_techParts:,.2f}")


st.subheader("Comparacion de compras entre proveedores")
grafico = px.bar(compras, x="proveedor", y="precio_total", color="proveedor", title="Total de Compras por Fecha y Proveedor")
st.plotly_chart(grafico)

st.subheader("Detalles de Registro")
st.dataframe(compras)

st.download_button("Descargar Reporte Completo", data=compras.to_csv(index=False), file_name="reporte_compras.csv", mime="text/csv")