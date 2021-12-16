# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 13:32:49 2021

@author: chels
"""
pip install streamlit
streamlit hello

import streamlit as st
import pandas as pd
import numpy as np

st.title('is it working')

st.text('i hope it is working')

df_hospital = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/hospital_info.csv')

df_inpatient = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/inpatient_2015.csv')

df_outpatient = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/outpatient_2015.csv')

st.dataframe(df_hospital)
st.dataframe(df_inpatient)
st.dataframe(df_outpatient)