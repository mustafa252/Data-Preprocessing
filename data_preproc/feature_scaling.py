
# libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import  OneHotEncoder, LabelEncoder, StandardScaler, Normalizer
from sklearn.compose import ColumnTransformer


# load data
data = pd.read_csv('/home/mustafa/Dropbox/WORK COURSES/machin learning/Codes/nba.csv')
print(data)
print(data.columns)


# extract Independent variables vectors
x = data[['Salary','Weight']]

x.dropna(inplace=True)
print(x)
print(x.shape)


# standardization
scaler = StandardScaler()
x = scaler.fit_transform(x)
print(x)


# normalization
scaler = Normalizer()
x = scaler.fit_transform(x)
print(x)









