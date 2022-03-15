# -*- coding: utf-8 -*-
"""
Created on Sun Mar 4 2022
@author: Spurti
"""

import pandas as pd
import numpy as np
import streamlit as st 
import datetime
from pandas.io.formats.style import Styler 
from pickle import load
#from sklearn.ensemble import RandomForestClassifier

st.title('Impact Prediction App')
st.sidebar.header('User Input Parameters')
def getNum(inp_str):
    num = ""
    for c in inp_str:
        if c.isdigit():
            num = num + c
    return num
 
def user_input_features():
    number = st.sidebar.text_input(label = 'Incident Number',value = 'INC')
    urgency = st.sidebar.selectbox("Urgency",('1 - High','2 - Medium','3 - Low'))
    priority = st.sidebar.selectbox("Priority",('1 - Critical','2 - High','3 - Moderate','4 - Low'))
    openedby = st.sidebar.text_input('openedBy',value = 'Opened by  ')
    syscreatedby = st.sidebar.text_input(label = "Incident Created By",value='Created by ')
    resolvedby = st.sidebar.text_input(label = "Resolved By",value='Resolved by ')
    callerid = st.sidebar.text_input(label = 'CallerId',value='Caller ')
    syscreatedD = st.sidebar.date_input(label = "Incident Created Date")
    openedD = st.sidebar.date_input(label = "Incident Open Date")
    syscreatedT = st.sidebar.time_input(label="Incident Created Time")
    openedT = st.sidebar.time_input(label = "Incident Open Time")
    
    syscreatedat = datetime.datetime.combine(syscreatedD,syscreatedT)
    openedat = datetime.datetime.combine(openedD,openedT)

    data = {'number':getNum(number),
            'caller_id':getNum(callerid),
            'opened_by':getNum(openedby),
            'sys_created_by':getNum(syscreatedby),
            'sys_created_at_day':syscreatedat.day,
            'urgency':getNum(urgency),
            'priority':getNum(priority),
            'resolved_by':getNum(resolvedby),
            'opened_at_hour':openedat.hour}
    st.header('User Input Details')
    st.markdown(
        f"""
        IncidentNumber : {number} \n
        Urgency : {urgency} \n
        Priority : {priority} \n
        OpenedBy : {openedby} \n
        SystemCreatedBy : {syscreatedby} \n
        ResolvedBy : {resolvedby} \n
        CallerId : {callerid} \n
        SystemCreatedAt : {syscreatedat} \n
        IncidentOpenAt : {openedat}
    """)
    features = pd.DataFrame.from_dict([data])
    return features
    
def main():    
    df = user_input_features()
    
    if(st.sidebar.button(label='Predict Impact')):
        st.subheader('User Input parameters')
        #st.table(df.assign(hack='').set_index('hack'))
        model = load(open('P:/Project/final folder/RandomForest_Model.sav', 'rb'))
        prediction = model.predict(df)
        if(prediction == 1):
            st.success('Impact Predicted is \n {} - High'.format(prediction))
        if(prediction == 2):
            st.success('Impact Predicted is \n {} - Medium'.format(prediction))
        if(prediction == 3):
            st.success('Impact Predicted is \n {} - Low'.format(prediction))

if __name__ == '__main__':
    main()
