import pandas as pd
import streamlit as sp
import utilidades as util
from matplotlib import pyplot
import seaborn as sns

#configuracion de encabezado de apgina
sp.set_page_config(
    page_title="Info Liga Colombiana",
    initial_sidebar_state="expanded",
    layout="centered",
    page_icon="🦩"
)

util.generarMenu()

sp.title("Datos de la liga Colombiana 2024")
ruta = "Data//tctClean.csv"
df = pd.read_csv(ruta)


tex = "Cantidad de goles por equipo"
util.informeDatos(df,tex)




