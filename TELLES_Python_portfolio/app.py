
import streamlit as st
import pandas as pd
st.title("MY FIRST APP")
st.write("welcome to my first app. Here, you will be able to access filtered information on yhe penguins.csv dataset, through their species and island!")
data = pd.read_csv("/Users/lissachaves/TELLES_PORTFOLIO/basic_streamlit_app/data/penguins.csv")
species = st.sidebar.selectbox('Select species', data['species'].unique())
island = st.sidebar.selectbox('Select island', data['island'].unique())
filtered_data = data[(data['species'] == species) & (data['island'] == island)]
st.write(filtered_data)
