#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.core.display import display, HTML
display(HTML("<style>.container { width:90% !important; }</style>"))


# ## @author: Ankit Pachauri
# ## @reference: https://towardsdatascience.com/stock-price-analysis-with-pandas-and-altair-ef1e178cc744

# In[2]:


import pandas as pd
import numpy as np
from pandas_datareader import data
import altair as alt


# ## use datareader to create Pandas dataframe

# In[3]:


start = '2020-01-01'
end = '2020-12-31'
source ='yahoo'

infosys = data.DataReader("INFY.NS", start= start, end= end, data_source =source).reset_index()

tcs = data.DataReader("TCS.NS", start= start, end= end, data_source =source).reset_index()

wipro = data.DataReader("WIPRO.NS", start= start, end= end, data_source =source).reset_index()


# In[4]:


infosys.head()


# In[5]:


infosys['Symbol']='INFY.NS'
tcs['Symbol']='TCS.NS'
wipro['Symbol']='WIPRO.NS'


# In[6]:


stocks = pd.concat([infosys[['Date', 'Close','Volume','Symbol']], tcs[['Date', 'Close','Volume','Symbol']],wipro[['Date', 'Close','Volume','Symbol']]],axis=0)


# In[7]:


(alt.Chart(stocks[stocks.Symbol=='INFY.NS']).mark_line().encode(x='Date', y='Close'))


# In[8]:


(alt.Chart(stocks).mark_line().encode(x='Date',y='Close',color='Symbol').properties(height=300,width=500))


# ### Resampling the data to get a refined and smooth line

# In[9]:


infosys_resampled = stocks[stocks.Symbol =='INFY.NS'].resample('7d',on='Date').mean().reset_index()


# In[10]:


(alt.Chart(infosys_resampled).mark_line().encode(x='Date',y='Close').properties(height=400,width=800))


# ### Closing price vs Volume for WIPRO stock

# In[11]:


price = (alt.Chart(stocks[stocks.Symbol=='INFY.NS']).mark_line().encode(x='Date',y='Close'))

volume = (alt.Chart(stocks[stocks.Symbol=='INFY.NS']).mark_line().encode(x='Date', y='Volume'))

price | volume


# In[ ]:




