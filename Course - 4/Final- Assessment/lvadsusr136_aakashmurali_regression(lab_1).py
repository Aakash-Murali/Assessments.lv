# -*- coding: utf-8 -*-
"""lvadsusr136_aakashmurali_Regression(lab 1).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1D5EauaIS-zFztNdiZv7v1TwIWEjcJt7A
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
from sklearn.metrics import accuracy_score, classification_report, precision_recall_fscore_support
from sklearn.metrics import precision_recall_curve,confusion_matrix, ConfusionMatrixDisplay
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier , RandomForestRegressor
from sklearn.ensemble import IsolationForest
import collections
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from imblearn.metrics import classification_report_imbalanced
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, accuracy_score, classification_report,silhouette_score
from sklearn.model_selection import KFold, StratifiedKFold
import random
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler , LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, precision_recall_fscore_support, precision_recall_curve
import warnings
warnings.filterwarnings("ignore")

df=pd.read_csv('https://raw.githubusercontent.com/Deepsphere-AI/LVA-Batch5-Assessment/main/Fare%20prediction.csv')
df.head()

#understanding the data
df.shape
df.info()

#checking for null/NA datas
df.isnull().sum()

#checking for duplicates that might affect prediction
df.duplicated().sum()

#to understand the relation between columns , we use heatmap and co-relation
corr=df.corr(numeric_only=True)
sns.heatmap(corr,annot=True,fmt='.2f')
plt.show()

#encoding the categorical Features
encode=LabelEncoder()
for col in df.select_dtypes(include='object').columns:
  df[col]=encode.fit_transform(df[col])
df.head()

#we are plotting box plot to see the outliers
for col in df.columns:
  sns.boxplot(df[col])
  plt.show()

'''def outliers(df1):
  for col in df1.select_dtypes(include=[int,float]).columns:
    q1=df1.quantile(0.25)
    q3=df1.quantile(0.75)
    iqr=q3-q1

    lower=q1-(1.5*iqr)
    upper=q3+(1.5*iqr)
    df1[col]=np.where(df1[col]>upper,upper,np.where(df1[col]<lower,lower,df1))
  return df1

clean_df=outliers(df.copy())
clean_df.head()'''

#scaling the values for better accuracy
scaler=MinMaxScaler()
for col in df.columns:
  df[col]=scaler.fit_transform(df[[col]])
df.head()

#dropping unwanted feature
df.drop('key',axis=1,inplace=True)

#dropping unwanted feature
x=df.drop('fare_amount',axis=1)
y=df['fare_amount']

#training the model
model=RandomForestRegressor()
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.3)
model.fit(xtrain,ytrain)
pred=model.predict(xtest)

print("MAE score : ",mean_absolute_error(ytest,pred))
print("\nMSE score : ",mean_squared_error(ytest,pred))
print("\nr2 score : ",r2_score(ytest,pred))

#plotting for better understanding
plt.scatter(ytest,pred,color='red')
plt.scatter(ytest,ytest,color='blue')
plt.show()