
# libraries
import numpy as np
import pandas as pd
import sklearn
from sklearn.impute import SimpleImputer


# load data
data = pd.read_csv('/home/mustafa/Dropbox/WORK COURSES/machin learning/Codes/nba.csv')
print(data.columns)

salary = data.loc[:,'Salary'].values
print(salary.shape)

salary = data.loc[:,:].values
print(salary.shape)

salary = data.loc[:,'Salary':].values
print(salary.shape)

salary = data.loc[1:3,'College':'Salary'].values
print(salary.shape)


## document
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html