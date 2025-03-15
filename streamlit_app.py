import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns
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
  st.bar_chart(df, x="Beli_Mobil", y="yield", color="site", stack=False)
  kor = df[['Usia', 'Memiliki_Mobil', 'Penghasilan']]
  korelasi = kor.corr()
  sns.heatmap(korelasi, annot=True, cmap='coolwarm')
  plt.title('Heatmap Korelasi')
  plt.show()
  sns.countplot(x=df['Beli_Mobil'])
  plt.title('Distribusi Variabel Target')
  plt.show()

