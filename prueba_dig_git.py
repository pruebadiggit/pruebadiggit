#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np


# In[10]:


df=pd.read_excel('C:/Users/2076222/OneDrive - TCS COM PROD/Documents/prueba_dig.xlsx')


# In[11]:


df['MILITAR']=np.where(df['CARGA']>1000,'Si','No')
df['FLAG_PASAJEROS']=np.where(df['PASAJEROS']>=1,1,0)


# In[12]:


df


# In[ ]:




