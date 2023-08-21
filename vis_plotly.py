import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px

data=pd.read_csv('tips.csv')

#1. Histogram for total bill

st.subheader('1. Histogram for total bill')

fig = px.histogram(data,x='total_bill')

st.plotly_chart(fig)

st.subheader('2. Histogram for total bill and color by sex')
fig = px.histogram(data,x='total_bill',color='sex')
st.plotly_chart(fig)

st.subheader('3. Histogram for total bill and color by variable categoric value')
data_types=data.dtypes
cat_cols=tuple(data_types[data_types == 'object'].index)
select=st.selectbox("Typ (3)",cat_cols)
fig = px.histogram(data,x='total_bill',color=select)
st.plotly_chart(fig)

st.subheader('4. Scatterplot for total bill and color by variable categoric value')
color=st.selectbox("Typ (4)",cat_cols)
fig = px.scatter(data,x='total_bill',y='tip',color=color)
st.plotly_chart(fig)

st.subheader('5. Sunburst chart on features')
path=st.multiselect("Typ (5)",cat_cols)
fig=px.sunburst(data,path=path)
st.plotly_chart(fig)