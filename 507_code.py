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

st.subheader('NY Hospital Data Pivot Table')
#Pivot table looking at effectiveness of care in NY hospitals
hospitals_ny_pivot = hospitals_ny.pivot_table(index=['state', 'city'],values=['effectiveness_of_care_national_comparison_footnote'],aggfunc='mean')
st.dataframe(hospitals_ny_pivot)
st.caption('There was not enough data for SBUH so we were not able to compare the effectiveness of care to other hospitals in NY.')

#Bar Chart
st.subheader('Hospital Type - NY')
bar1 = hospitals_ny['hospital_type'].value_counts().reset_index()
st.dataframe(bar1)

st.caption('The majority of hospitals in NY are acute care, followed by psychiatric')


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

#Showing table for inpatient DRGs at only SBUH
st.subheader('Inpatient DRGs at SBUH')
st.dataframe(common_discharges)

#Creating table for most common outpatient DRGs at SBUH
col1, col2 = st.beta_columns(2)
col1.subheader('Top 10 common outpatient DRGs at SBUH')
col1.dataframe(top10_inpatient)
st.caption('The most common outpatient DRG at SBUH was for craniotomy and endovascular intracranial procedures with MCC.')

#Creating table for least common outpatient DRGs at SBUH
col2.subheader('Bottom 10 common outpatient DRGs at SBUH')
col2.dataframe(bottom10_inpatient)
st.caption('The least common outpatient DRG at SBUH was for other multiple significant trauma with MCC/CC.')

#Looking at DRGs and average costs for Stony Brook
cost_discharges = inpatient_ny[inpatient_ny['provider_name'] == 'UNIVERSITY HOSPITAL ( STONY BROOK )']
cost_discharges = cost_discharges.groupby('drg_definition')['average_total_payments'].sum().reset_index()
top10_costs_inpatient = cost_discharges.head(10)
bottom10_costs_inpatient = cost_discharges.tail(10)

#Showing table for inpatient DRG costs at only SBUH
st.subheader('Inpatient DRG costs at SBUH')
st.dataframe(cost_discharges)

#Creating table for most expensive inpatient DRGs at SBUH
col1, col2 = st.beta_columns(2)
col1.subheader('Most expensive inpatient DRGs at SBUH')
col1.dataframe(top10_costs_inpatient)
st.caption('The most expensive inpatient DRG at SBUH was for ecmo or trach.')

#Creating table for least expensive inpatient DRGs at SBUH
col2.subheader('Cheapest inpatient DRGs at Stony SBUH')
col2.dataframe(bottom10_costs_inpatient)
st.caption('The cheapest inpatient DRG at SBUH was for sign and symptoms without MCC')



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

#Showing outpatient DRGS at only SBUH
st.subheader('Outpatient DRGs at SBUH')
st.dataframe(common_discharges_outpatient)

#Creating table for most common DRGs at SBUH
col1, col2 = st.beta_columns(2)
col1.subheader('Top 10 common outpatient DRGs at SBUH')
col1.dataframe(top10_discharges_outpatient)
st.caption('The most common outpatient DRG at SBUH was for Level I echocardiogram without contrast.')

#Creating table for least common DRGs at SBUH
col2.subheader('Bottom 10 common outpatient DRGs at SBUH')
col2.dataframe(bottom10_discharges_outpatient)
st.caption('The least common outpatient DRG at SBUH was for Level I electronic analysis of devices.')

#Looking at DRGs and average costs for Stony Brook
cost_discharges_outpatient = outpatient_ny[outpatient_ny['provider_name'] == 'University Hospital ( Stony Brook )']
cost_discharges_outpatient = cost_discharges_outpatient.groupby('apc')['average_total_payments'].sum().reset_index()
top10_costs_outpatient = cost_discharges_outpatient.head(10)
bottom10_costs_outpatient = cost_discharges_outpatient.tail(10)

#Showing outpatient DRG costs for only SBUH
st.subheader('Outpatient DRGs costs at SBUH')
st.dataframe(cost_discharges_outpatient)

#Creating table for most expensive outpatient DRGs
col1, col2 = st.beta_columns(2)
col1.subheader('Most expensive outpatient DRGs at SBUH')
col1.dataframe(top10_costs_outpatient)
st.caption('The most expensive outpatient DRG at SBUH was for Level IV endoscopy upper airway.')

#Creating table for least expensive outpatient DRGs
col2.subheader('Cheapest outpatient DRGs at SBUH')
col2.dataframe(bottom10_costs_outpatient)
st.caption('The least expensive outpatient DRG at SBUH was for Level I electronic analysis of devices.')
