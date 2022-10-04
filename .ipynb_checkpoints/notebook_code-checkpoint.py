

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# fetch csv file at url 'https://github.com/fivethirtyeight/data/blob/master/polls/pres_pollaverages_1968-2016.csv' and read into DataFrame
df = pd.read_csv('https://github.com/fivethirtyeight/data/blob/master/polls/pres_pollaverages_1968-2016.csv?raw=true')

# print first 5 rows of DataFrame
print(df.head())

# print the shape of the DataFrame
print(df.shape)

# print the columns of the DataFrame
print(df.columns)

# print the data types of the DataFrame
print(df.dtypes)

# print the summary statistics of the DataFrame
print(df.describe())

# print the info of the DataFrame
print(df.info())

# print the number of non-missing values in each column
print(df.count())

# print the number of missing values in each column
print(df.isnull().sum())

# print the number of unique values in each column
print(df.nunique())

