import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import datetime
import os

db_path = "/Users/ignacioviera/Desktop/automatizacion-reporte-compras/reporte_compras.db"


conn = sqlite3.connect(db_path)

compras = pd.read_sql_query("SELECT * FROM compras", conn)

total_compras = compras["precio_total"].sum()
st.subheader("Gasto Total: ")
st.subheader(f"${total_compras:,.2f}")


total_logiMax = compras[compras["proveedor"] == "LogiMax"]["precio_total"].sum()
total_megaTools = compras[compras["proveedor"] == "MegaTools"]["precio_total"].sum()
total_novaIndustrias = compras[compras["proveedor"] == "NovaIndustrias"]["precio_total"].sum()
total_techParts = compras[compras["proveedor"] == "TechParts"]["precio_total"].sum()

st.subheader("Total de compras por proveedor: ")

col1, col2, col3, col4 = st.columns(4)
with col1: 
    st.metric("gasto logimax", f"${total_logiMax:,.2f}")

with col2: 
    st.metric("gasto megatools", f"${total_megaTools:,.2f}")

with col3: 
    st.metric("gasto nova industrias", f"${total_novaIndustrias:,.2f}")

with col4: 
    st.metric("gasto tech parts", f"${total_techParts:,.2f}")







grafico = px.bar(compras, x="proveedor", y="precio_total", color="proveedor", title="Total de Compras por Fecha y Proveedor")
st.plotly_chart(grafico)

st.dataframe(compras)
