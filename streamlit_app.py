import streamlit as st
import pandas as pd
import numpy as np

st.title('🎈 App Name')

st.info('Hello world!')

with st.expander('Data'):
  df = pd.read_csv('https://raw.githubusercontent.com/M-Fathul/startingML/refs/heads/master/calonpembelimobil.csv')
  df
  st.write('**features**')
  X = df.drop(['Beli_Mobil', 'ID'], axis=1)
  X
  
  st.write('**Class**')
  y = df.Beli_Mobil
  y

with st.sidebar:
  Status = st.selectbox('Status', (0, 1, 2, 3))
  Kelamin = st.selectbox('Status', (0, 1))
  Usia = st.number_input("Insert age", value=None, placeholder="Type a number...")
