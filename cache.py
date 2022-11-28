import streamlit as st
import pandas as pd

st.title('Streamlit con cache')

DATA_URL = 'https://raw.githubusercontent.com/enriquevgo/streamlit-labs/master/dataset.csv?token=GHSAT0AAAAAAB3WVVSV34QS5L5N2PDUWUKOY4EJASA'

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

data_load_state = st.text('Loading data ...')

data = load_data(500)

data_load_state.text('Done ...')
st.dataframe(data)