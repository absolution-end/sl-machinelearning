import streamlit as st
import pandas as pd
st.title('Belto-B')
# st.title('')
st.write('Product work on image/video analysis model')
df =pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
df
