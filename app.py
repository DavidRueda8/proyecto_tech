import pandas as pd
import utilidades as util
import streamlit as sp
from PIL import Image



#Página de presentacion
sp.set_page_config(
    page_title="Info Liga Colombiana",
    initial_sidebar_state="expanded",
    layout="wide",
    page_icon="🏆"
)

#Llamamos la funcion
util.generarMenu()

#estrutura de presentacion

left_col, center_col, right_col = sp.columns([1,4,1],vertical_alignment="center")

#edito la columna central

with center_col:
    sp.title("Informe de la liga colombiana 2024-2")
    sp.write("""
    En este espacio se peude mostrar cual fue el desempeño de los equipos durante la liga BtPlay en el año 2024-2         
             
             """)
    imagen2 = Image.open("Media\image.2png.jpg")
    sp.image(imagen2, use_container_width=True, width=500, caption="Seleccion Colombia")
