import streamlit as st
import pandas as pd
import openpyxl
import numpy as np

st.title("Asta random")
    
uploaded_file = st.file_uploader("Carica file excel con le quotazioni aggiornate", type=["xlsx"])
dropped_lines_df = pd.DataFrame()
random_seed = np.random.randint(0, 100)
st.write(str(random_seed) + " - Numero di emergenza")
np.random.seed(random_seed)
i = 0

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    soglia_minima = 2
    df.columns = df.iloc[0,:].to_list()
    df = df.iloc[1:,:]
    df = df[["RM",	"Nome",	"Squadra",	"Qt.A"]]
    df = df[df["Qt.A"]>soglia_minima]
    df = df.sample(frac=1)
    df.reset_index(drop=True, inplace=True)
    
    if st.button("Estrai un giocatore"):
        st.write("Giocatori mancanti:", len(df)-i-1)
        st.write(df.iloc[:i,:])

        
    
