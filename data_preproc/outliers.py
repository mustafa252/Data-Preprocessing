
# libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import  OneHotEncoder, LabelEncoder, StandardScaler, Normalizer
from sklearn.compose import ColumnTransformer
import matplotlib.pyplot as plt

# load data
data = pd.read_csv('/home/mustafa/Dropbox/WORK COURSES/machin learning/Codes/nba.csv')
print(data)
print(data.columns)


# extract Independent variables vectors
x = data['Salary']

x.dropna(inplace=True)
print(x)
print(x.shape)

# show data outlier in histogram
plt.hist(x, bins=15)
plt.show()

# quantile the data
lowerLim = x.quantile(0.05)
print(lowerLim)

higherLim = x.quantile(0.95)
print(higherLim)


# show outliers
outl_1 = x[x < lowerLim]
print(outl_1)

outl_2 = x[x > higherLim]
print(outl_2)

# show outliers
x_new = x[(x > lowerLim) & (x < higherLim)]
print(x_new)

