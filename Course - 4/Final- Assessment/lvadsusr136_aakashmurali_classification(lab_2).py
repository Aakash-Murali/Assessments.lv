# -*- coding: utf-8 -*-
"""lvadsusr136_aakashmurali_classification(lab 2).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1z7Po2PIYYkNYUPipzHFHVd-sU_01ruNR
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

df=pd.read_csv('https://raw.githubusercontent.com/Deepsphere-AI/LVA-Batch5-Assessment/main/penguins_classification.csv')
df.head()

#understanding the data
df.shape
df.info()

#checking for null values
df.isnull().sum()
df=df.dropna()
#dropping null values because of overfitting

#replacing the NA values with the mean of that feature
'''df['bill_depth_mm']=df['bill_depth_mm'].fillna(df['bill_depth_mm'].mean())
df.isnull().sum()'''

#checking for duplicated data
df.duplicated().sum()

#checking for outliers that might affect the model
for col in df.columns:
  sns.boxplot(df[col])
  plt.show()

#scaling values because of overfitting
scale=MinMaxScaler()
for col in df.select_dtypes(include=[int,float]).columns:
  df[col]=scale.fit_transform(df[[col]])
df.head()

#encoding the categorical data for better predcition
encode=LabelEncoder()
for col in df.select_dtypes(include='object').columns:
  df[col]=encode.fit_transform(df[col])
df.head()



#understanding the co-relations
corr=df.corr()
sns.heatmap(corr,annot=True,fmt='.2f')
plt.show()

x=df.drop('species',axis=1)
y=df['species']

model=RandomForestClassifier()
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.3)
model.fit(xtrain,ytrain)
pred=model.predict(xtest)

print("Accuracy score: ",accuracy_score(ytest,pred))
print("\nprecision score: ",precision_score(ytest,pred))
print("\nrecall score: ",recall_score(ytest,pred))
print("\n\nConfusion Matrix score: ",confusion_matrix(ytest,pred))