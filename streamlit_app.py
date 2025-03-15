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
  Kelamin = st.selectbox('Jenis kelamin', (0, 1))
  Usia = st.number_input("Usia", value=None, placeholder="...")
  Memiliki_Mobil = st.number_input("Jumlah mobil yang dimiliki", value=None, placeholder="...")
  Penghasilan = st.number_input("penghasilan juta perthaun ", value=None, placeholder="...")
  data = {'Status': Status, 'Kelamin': Kelamin, 'Usia': Usia, 'Memiliki_Mobil': Memiliki_Mobil, 'Penghasilan': Penghasilan}
  input_df = pd.DataFrame(data, index=[0])
input_df
target_mapper = {0: 'tidak membeli mobil', 1:'membeli mobil'}
def terget_encoder(val, target):
  return target[val]
klasifikasi = y.apply(terget_encoder)
klasifikasi
