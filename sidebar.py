import streamlit as st
import numpy as np
import pandas as pd

# crear title de la app web
st.title('Streamlit con Sidebar')
sidebar = st.sidebar
sidebar.title('Titulo de barra lateral')

st.header('Header de mi app')
sidebar.write('Información de mi app')

if sidebar.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randint(1,10, size=(20,3)),
        columns=['a','b','c'])
    
    st.dataframe(chart_data)
