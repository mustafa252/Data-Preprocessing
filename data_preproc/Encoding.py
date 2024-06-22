
# libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import  OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer


# load data
data = pd.read_csv('/home/mustafa/Dropbox/WORK COURSES/machin learning/Codes/nba.csv')
print(data)
print(data.columns)


# extract Independent variables vectors
x = data.drop(['Salary','Name','Position','College','Height'], axis=1)
x.dropna(inplace=True)
print(x)
print(x.columns.get_loc('Team'))


# One Hot Encoding
team = ColumnTransformer( transformers=[('encoder', OneHotEncoder(),
                        [0])],
                        remainder='passthrough')

x = np.array(team.fit_transform(x))
print(x)
print(x.shape)


#############################################################################################

y = data['Team']
print(y.shape)
# Label Encoder
le = LabelEncoder()
y = le.fit_transform(y)
print(y)














