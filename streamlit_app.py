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
  source = df
  st.bar_chart(source, x="Beli_Mobil", y="none", color="Beli_Mobil", stack=False)
