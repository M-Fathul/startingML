import streamlit as st
import pandas as pd

st.title('🎈 App Name')

st.info('Hello world!')

with st.expander('Data'):
  df = pd.read_csv('https://raw.githubusercontent.com/M-Fathul/startingML/refs/heads/master/calonpembelimobil.csv')
  df
  st.write('**Class**')
  X = df.drop(['Beli_Mobil', 'ID'], axis=1)
  X
  st.write('**features**')
  y = df.Beli_Mobil
  y

