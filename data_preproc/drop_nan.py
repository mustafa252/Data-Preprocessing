
# libraries
import numpy as np
import pandas as pd
import sklearn
from sklearn.impute import SimpleImputer


# load data
data = pd.read_csv('/home/mustafa/Dropbox/WORK COURSES/machin learning/Codes/nba.csv')
print(data.columns)

##############################################################################
###### handling missing data

''' by pandas'''
# data.dropna(inplace=True)
# print(data.info)

''' by sklearn'''
print(data.isnull().sum())
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
salary = data.loc[:,'Salary':].values
imputer.fit(salary)
salary = imputer.transform(salary)
print(salary)
print(salary.shape)






