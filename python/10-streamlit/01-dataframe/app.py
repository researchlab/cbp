import streamlit as st
import numpy as np 
import pandas as pd 
st.title("dataFrame")
df = pd.DataFrame({
    'first':[5,6,7,8,9],
    'second':[50,60,70,80,90]
    })

st.write(df)

st.write('show dataFrame')

df



