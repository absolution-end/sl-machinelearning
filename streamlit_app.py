import streamlit as st
import pandas as pd
st.title('Belto-B')
# st.title('')
st.write('Product work on image/video analysis model')
with st.expander('Data'):
  st.write('**Raw Data**')
  df =pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
  df

with st.expander('Data Visualization'):
  st.bar_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')

# Data preparations
with st.sidebar:
  st.header("Input Features")
  island = st.selectbox('Island', ('Biscoe', "Dream", 'Torgersen'))
  gender = st.selectbox('Gender', ('male', 'female'))
  bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.1, 43.9)
  bill_depth_mm = st.slider('Bill Depth', 13.1, 21.5, 17.2)
  flipper_length_mm = st.slider('Flipper length(mm)', 172.0,231.0,201.0)
  body_mass_g = st.slider('Body mass(g)', 2700.0,6300.0,4207.0)
