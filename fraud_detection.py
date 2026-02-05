# -*- coding: utf-8 -*-
"""
Created on Wed Aug  6 10:29:41 2025

@author: Motheo Moshageng
"""

import pandas as pd
import joblib 
import streamlit as st

# load the model
model = joblib.load('model_lr.joblib')

st.title('FRAUD DETECTION APP')

st.markdown('PLEASE FILL IN THE DETAILS AND SUBMIT')

st.divider()

transaction_type = st.selectbox('Transaction Type',[1,2,3,4,5])
amount = st.number_input('Amount',min_value=0.0,value=1000.0)
oldBalanceOrg = st.number_input('Old Balance (Sender)',min_value=0.0,value=10000.0,key='oldBalanceOrg')
newBalanceOrig = st.number_input('New Balance (Sender)',min_value=0.0,value=1000.0,key='newBalanceOrig')
oldBalanceDest = st.number_input('Old Balance (Reciever)',min_value=0.0,value=0.0,key='oldBalanceDest')
newBalanceDest = st.number_input('New Balance(Reciever)',min_value=0.0,value=0.0,key='newBalanceDest')
balanceDiffOrig = st.number_input('Balance Difference ', min_value=0.0,value=0.0,key='balanceDiffOrig')
balanceDiffDest = st.number_input('Balance Difference ',min_value=0.0,value=0.0,key='balanceDiffDest')

if st.button('predict'):
    input_data = pd.DataFrame([{
        'type' : transaction_type,
        'amount' : amount,
        'oldBalanceOrg': oldBalanceOrg,
        'newBalanceOrig' : newBalanceOrig,
        'oldBalanceDest' : oldBalanceDest,
        'newBalanceDest' : newBalanceDest,
        'balanceDiffOrig': balanceDiffOrig,
        'balanceDiffDest' : balanceDiffDest
        }])
    
    prediction = model.predict(input_data)[0]
    
    st.subheader(f'Prediction : "{int(prediction)}"')
    
    if prediction == 1:
        st.error('this transaction is elegible of fraud')
    else:
        st.success('this transaction is not fraud')
    
