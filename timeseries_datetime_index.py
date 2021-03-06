# -*- coding: utf-8 -*-
"""timeSeries_datetime_index.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q0mkt0NLzHxlFe8ZhVMm6k3ICL9Zmh18

<h1 style="color:blue" align="center">Pandas Time Series : DateTimeIndex</h1>
"""

import pandas as pd
df=pd.read_csv("/content/aapl.csv")
df.head(2)
type(df.Date[0])

#  we have to convert it into date formate
df = pd.read_csv("/content/aapl.csv",parse_dates=["Date"])
df.head(2)
# type(df.Date[0])

# in time seriers we date column to be index

df = pd.read_csv("/content/aapl.csv",parse_dates=["Date"], index_col="Date")
df.head(2)

#  to check the index
df.index

"""<h3 style="color:purple">What is DatetimeIndex? Benefits of it</h3>

<h4> (1) Partial Date Index: Select Specific Months Data</h4>
"""

df['03-12-2020']

# for example i want to get the data of january 2017 
df["2020-02"]

df['2020-02'].head()

"""<h4>Average price of aapl's stock in June, 2017</h4>"""

df['2020-02'].Open.mean()

df['2020'].head(2)

"""<h4>(2) Select Date Range</h4>"""

df['2020-02-11':'2020-03-11']

df['2017-01']

"""<h3 style="color:purple">Resampling</h3>"""

#  the given data is of days but we want to get of months data than we use resampling
# for month use M and for week use W
df['Close'].resample('W').mean().head()
# to plot the graph
df['Close'].resample('W').mean().plot()

# df['2016-07']

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
df['Close'].plot()

df['Close'].resample('M').mean().plot(kind='bar',)