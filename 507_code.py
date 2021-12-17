# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 13:32:49 2021

@author: chels
"""

import streamlit as st
import pandas as pd
import numpy as np

#Title of app
st.title('HHA 507 Final Assignment')

df_hospital = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/hospital_info.csv')

df_inpatient = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/inpatient_2015.csv')

df_outpatient = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/outpatient_2015.csv')

#Introduce first dataset - hospitals
st.header('Hospital Data Preview')
st.dataframe(df_hospital)

#Look at only NY hospitals
hospitals_ny = df_hospital[df_hospital['state'] == 'NY']

#Look at columns and counts
hospitals_ny.info()

#Clean out data
hospitals_ny.dropna()

#Pivot table looking at effectiveness of care in NY hospitals
hospitals_ny_pivot = hospitals_ny.pivot_table(index=['state', 'city'],values=['effectiveness_of_care_national_comparison_footnote'],aggfunc='mean')
st.dataframe(hospitals_ny_pivot)

#Introduce second dataset - inpatient
st.header('Inpatient Data Preview for NY')

#Clean dataset
df_inpatient.dropna()

#Look at only NY hospitals
inpatient_ny = df_inpatient[df_inpatient['provider_state'] == 'NY']
st.dataframe(inpatient_ny)

#Looking at common discharges and DRGs for Stony Brook
common_discharges = inpatient_ny[inpatient_ny['provider_name'] == 'UNIVERSITY HOSPITAL ( STONY BROOK )']
common_discharges = common_discharges.groupby('drg_definition')['total_discharges'].sum().reset_index()
top10_inpatient = common_discharges.head(10)
bottom10_inpatient = common_discharges.tail(10)

st.header('DRGs')
st.dataframe(common_discharges)

col1, col2 = st.beta_columns(2)
col1.header('Top 10 common DRGs')
col1.dataframe(top10_inpatient)
col2.header('Bottom 10 common DRGs')
col2.dataframe(bottom10_inpatient)

#Looking at DRGs and average costs for Stony Brook
cost_discharges = inpatient_ny[inpatient_ny['provider_name'] == 'UNIVERSITY HOSPITAL ( STONY BROOK )']
cost_discharges = cost_discharges.groupby('drg_definition')['average_total_payments'].sum().reset_index()
top10_costs_inpatient = cost_discharges.head(10)
bottom10_costs_inpatient = cost_discharges.tail(10)

st.header('DRGs costs')
st.dataframe(cost_discharges)

col1, col2 = st.beta_columns(2)
col1.header('Most expensive DRGs')
col1.dataframe(top10_costs_inpatient)
col2.header('Cheapest DRGs')
col2.dataframe(bottom10_costs_inpatient)


#Introduce third dataset - outpatient
st.header('Outpatient Data Preview for NY')

#Clean dataset
df_outpatient.dropna()

#Look at only NY hospitals
outpatient_ny = df_outpatient[df_outpatient['provider_state'] == 'NY']
st.dataframe(outpatient_ny)

#Looking at common discharges and DRGs for Stony Brook
common_discharges_outpatient = outpatient_ny[outpatient_ny['provider_name'] == 'University Hospital ( Stony Brook )']
common_discharges_outpatient = common_discharges_outpatient.groupby('apc')['outpatient_services'].sum().reset_index()
top10_discharges_outpatient = common_discharges_outpatient.head(10)
bottom10_discharges_outpatient = common_discharges_outpatient.tail(10)

st.header('DRGs')
st.dataframe(common_discharges_outpatient)

col1, col2 = st.beta_columns(2)
col1.header('Top 10 common DRGs at Stony Brook Hospital')
col1.dataframe(top10_discharges_outpatient)
col2.header('Bottom 10 common DRGs at Stony Brook Hospital')
col2.dataframe(bottom10_discharges_outpatient)

#Looking at DRGs and average costs for Stony Brook
cost_discharges_outpatient = outpatient_ny[outpatient_ny['provider_name'] == 'University Hospital ( Stony Brook )']
cost_discharges_outpatient = cost_discharges_outpatient.groupby('apc')['average_total_payments'].sum().reset_index()
top10_costs_outpatient = cost_discharges_outpatient.head(10)
bottom10_costs_outpatient = cost_discharges_outpatient.tail(10)

st.header('DRGs costs')
st.dataframe(cost_discharges_outpatient)

col1, col2 = st.beta_columns(2)
col1.header('Most expensive outpatient DRGs at Stony Brook Hospital')
col1.dataframe(top10_costs_outpatient)
col2.header('Cheapest outpatient DRGs at Stony Brook Hospital')
col2.dataframe(bottom10_costs_outpatient)
