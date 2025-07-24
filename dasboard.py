import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import datetime
import os

db_path = "/Users/ignacioviera/Desktop/automatizacion-reporte-compras/reporte_compras.db"

conn = sqlite3.connect(db_path)

compras = pd.read_sql_query("SELECT * FROM compras", conn)

grafico = px.bar(compras, x="proveedor", y="precio_total", color="proveedor", title="Total de Compras por Fecha y Proveedor")
st.plotly_chart(grafico)

st.dataframe(compras)
