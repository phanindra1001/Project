# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 18:53:35 2022

@author: Phani Ullamgunta
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from pickle import dump
import warnings
warnings.filterwarnings('ignore')

#import the file which was saved during EDA
df = pd.read_csv('FinalData_incidentlog.csv')

Y = df.iloc[:,9]
X = df.iloc[:,0:9]

model = RandomForestClassifier(n_estimators=400,max_features=3)
model.fit(X,Y)

dump(model, open('P:/Project/final folder/RandomForest_Model.sav', 'wb'))
