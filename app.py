import streamlit as st
import pandas as pd
import openpyxl

st.title("Asta random")
    
uploaded_file = st.file_uploader("Carica file excel con le quotazioni aggiornate", type=["xlsx"])
dropped_lines_df = pd.DataFrame()


if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    soglia_minima = 2
    df.columns = df.iloc[0,:].to_list()
    df = df.iloc[1:,:]
    df = df[["RM",	"Nome",	"Squadra",	"Qt.A"]]
    df = df[df["Qt.A"]>soglia_minima]
    if st.button("Estrai un giocatore"):
        random_index = random.randint(0, len(df) - 1)
        random_line = df.iloc[random_index]
        df.drop(index=random_line.name, inplace=True)
        dropped_lines_df = dropped_lines_df.append(random_line)
        st.write("Giocatori rimasti:", len(df))
        st.write(dropped_lines_df)
        
    
