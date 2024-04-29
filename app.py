import streamlit as st
import pandas as pd

view=[100, 200, 150]



st.write('#Youtube view')
st.write('### bar chart')
view

st.bar_chart(view)

sview=pd.Series(view)
sview