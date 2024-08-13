#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np


# In[5]:


data=pd.read_csv(r'C:\Users\User\Downloads\diabetes_prediction_dataset.csv')
data.head()


# In[6]:


data.shape


# In[7]:


data.isna().sum()


# In[8]:


data.info()


# In[10]:


data.describe()


# In[11]:


data.isnull().sum()


# In[12]:


import matplotlib.pyplot as plt


# In[14]:


data[(data["age"]==0)&(data["blood_glucose_level"]=="no")]["blood_glucose_level"].max()


# In[17]:


data.gender.replace(['male','female'],[1,0],inplace=true)
data.head()


# In[18]:


data["smoking_history"].unique()


# In[21]:


data.gender.replace(['never','no info','current','former','ever','not current'],[0,1,2,3,4,5])


# In[ ]:





# In[23]:


x=np.array(data.filter(['age','gender','hypertension',]))


# In[24]:


y=np.array(data.filter(['diabetes'],axis=1))


# In[25]:


x_1,x_test,y_1,y_test=train_test_split(x,y,test_size=0.3)
x_tr,x_cv,y_tr,y_cv=train_test_split(x_1,y_1,test_size=0.3)


# In[29]:


x_train,x_test,y_train,y_test=train_test_split (x,y,test_size=0.33,random_state=42)


# In[32]:


non_numeric_cols=data.select_dtypes(exclude=['number']).columns


# In[34]:


x=np.array(data.drop('diabetes',axis=1))
y=np.array(data['diabetes'])


# In[35]:


x=data.drop('diabetes',axis=1)
y=data['diabetes']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,stratify=y,random_state)


# In[36]:


model=svc(probability=true,random_state=0)
model.fit(x_train,y_train)


# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[38]:


plt.figure(figsize=(8,4))
sns.barplot(x=data['male'],y=data['female'])


# In[ ]:





# In[ ]:




