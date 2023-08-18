import streamlit as st
import pandas as pd
import openpyxl
import numpy as np

st.title("Asta random")

random_seed = st.text_area("inserisci un numero a tuo piacimento")
random_seed = int(random_seed)

if 'i' not in st.session_state:
    st.session_state['i'] = 0

uploaded_file = st.file_uploader("Carica file excel con le quotazioni aggiornate", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    soglia_minima = 2
    df.columns = df.iloc[0,:].to_list()
    df = df.iloc[1:,:]
    df = df[["RM",	"Nome",	"Squadra",	"Qt.A"]]
    df = df[df["Qt.A"]>=soglia_minima]
    np.random.seed(random_seed)
    df = df.sample(frac=1)

    if st.button("Estrai un giocatore"):
        i = st.session_state['i']
        st.write("Giocatori mancanti:", len(df)-i-1)
        st.write(df.iloc[:i+1,:])
        st.session_state['i'] = i+1


        
    
