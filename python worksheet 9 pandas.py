#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np


# In[5]:


exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin',
'Jonas'],
 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}


# In[8]:


df = pd.DataFrame(exam_data, index = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"])


# In[9]:


print(df)


# In[11]:


print(df[0:5])


# In[31]:


selection = df[['name','score']]
print(selection)


# In[37]:


print(selection[3:5:9])


# In[40]:


print(df.loc[(df['score'] > 15) & (df['score'] <= 20)])


# In[ ]:




