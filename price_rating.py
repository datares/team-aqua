#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import chart_studio


# In[3]:


df_main = pd.read_csv('C:/Users/zoeym/Downloads/clean_amazon_data.csv')


# In[4]:


df_main.columns


# In[12]:


fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(x = df_main['price'], y = df_main['rating'])
plt.title("Price vs Rating")
plt.xlabel("Price")
plt.ylabel("Rating")

plt.show()


# In[ ]:




