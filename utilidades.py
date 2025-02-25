import pandas as pd
import streamlit as sp
from PIL import Image
from matplotlib import pyplot
import seaborn as sns

def generarMenu():
    with sp.sidebar:
        col1, col2 = sp.columns(2)
        with col1:
            imagen = Image.open("Media/image.png")
            sp.image(imagen, use_container_width=False, width=80)
        with col2:
            sp.header("Liga Betplay 2025")
        
        sp.page_link("app.py",label="Home", icon="🏠")
        sp.page_link("Pages/informe.py",label="Informe", icon="🗒️")



def informeDatos(df,titulo):
    df2 = pd.DataFrame(df)
     #Configurar la visualización
    col1, col2, col3, = sp.columns([0.5,5,0.5],
                  vertical_alignment="top")
    with col2:
        sp.markdown(titulo)
        df2.set_index("Local",inplace=True)
        sp.write(df, unsafe_allow_html=False)
        sp.markdown("Gráfico de barras")



        sns.set_style("whitegrid")
        total = df2.groupby("Local")[["Goles local", 
                                      "Goles visitante"]].sum()
        goles = pd.DataFrame(total)
        goles["Goles Totales"] = goles["Goles local"] + goles["Goles visitante"]
        goles = goles.reset_index()

        resultado = goles.groupby(["Local"]).sum()
        resultado.plot(kind="bar",figsize=(10,10))
        pyplot.tight_layout()
        sp.pyplot(pyplot)



    
        

            
