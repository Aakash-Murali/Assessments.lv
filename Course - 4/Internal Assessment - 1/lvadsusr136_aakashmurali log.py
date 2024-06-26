# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1V5B2qNdPnYDOHYreT76dVJfDbyD60Ucl
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler , StandardScaler
from sklearn.metrics import accuracy_score, classification_report, precision_recall_fscore_support
from sklearn.metrics import precision_recall_curve,confusion_matrix, ConfusionMatrixDisplay
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error

df=pd.read_csv('https://raw.githubusercontent.com/Deepsphere-AI/LVA-Batch5-Assessment/main/booking.csv')
df.head()

df.isnull().sum() # there are totally 18 and 48 na values in roomtype and average price
df['room type'].fillna(df['room type'].mode())
df['average price'].fillna(df['average price'].mean())

df.drop('Booking_ID',axis=1,inplace=True)

num_cols=df.select_dtypes(include=['int64','float64']).columns
categorical_cols=df.select_dtypes(include='object').columns
encoded=pd.get_dummies(df,columns=categorical_cols)
encoded[num_cols]=MinMaxScaler().fit_transform(encoded[num_cols])
boolean_cols=encoded.select_dtypes(include='boolean').columns
encoded[boolean_cols]=encoded[boolean_cols].astype(int)


encoded.drop(['booking status_Canceled','booking status_Not_Canceled'],axis=1,inplace=True)
encoded['booking status']=df['booking status']
encoded['booking status']=encoded['booking status'].map({'Not_Canceled':1,'Canceled':0})

encoded.head()

x=encoded.drop('Booking status')
y=encoded['booking status']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
model=LinearRegression()
model.fit(x_train,y_train)
pred = model.predict(x_test)