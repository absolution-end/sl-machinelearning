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
