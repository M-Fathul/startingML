import streamlit as st
import pandas as pd

st.title('🎈 App Name')

st.info('Hello world!')

df = pd.read_csv('https://raw.githubusercontent.com/M-Fathul/startingML/refs/heads/master/calonpembelimobil.csv')
df
