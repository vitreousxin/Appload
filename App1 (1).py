
# coding: utf-8

# In[129]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import seaborn as sns
from sklearn import metrics
import random
import os
from sklearn.linear_model import LinearRegression
get_ipython().run_line_magic('matplotlib', 'inline')


# In[130]:


from google.colab import files
uploaded = files.upload()


# In[ ]:


df=pd.read_csv('googleplaystore.csv')


# In[132]:


df.head()


# In[133]:


print(df.shape)


# In[134]:


df.info()


# In[135]:


df.isnull().sum()


# In[ ]:


df.dropna(how = 'any',inplace = True)


# In[137]:


df.info()


# In[138]:


print(df.shape)


# In[139]:


df['Rating'].describe()


# In[140]:


plt.figure(figsize = (11,8))
sns.distplot(df['Rating'])


# In[141]:


print(len(df['Category'].unique()),"categories")
print("\n",df['Category'].unique())


# In[142]:


print("Skewness : %f" % df['Rating'].skew())
print("Kurtosis : %f" % df['Rating'].kurt())


# In[143]:


graph= sns.countplot(x="Category",data=df, palette = "Set1")
graph.set_xticklabels(graph.get_xticklabels(), rotation=90)
graph 


# In[144]:


df.Size.value_counts()


# In[ ]:


def SizeChange(size):
  x=0
  if 'M' in size:
    x = size[:-1]
    x = float(x)*1000000
    return(x)
  elif 'k' in size:
    x = size[:-1]
    x = float(x)*1000
    return(x)
  else:
    return None

df['Size'] = df['Size'].map(SizeChange)


# In[146]:


df.Size.value_counts()


# In[ ]:


df.Size.fillna(method = 'ffill', inplace = True)


# In[148]:


df.Size.value_counts()


# In[149]:


print(len(df['Installs'].unique()),"categories")
df['Installs'].value_counts()


# In[150]:


df.Installs.unique()


# In[151]:


df.Installs.head()


# In[ ]:


df.Installs = df.Installs.apply(lambda x: x.replace(',',''))
df.Installs = df.Installs.apply(lambda x: x.replace('+',''))
df.Installs = df.Installs.apply(lambda x: int(x))


# In[153]:


df.Installs.head()


# In[ ]:


InstallsVal = sorted(list(df['Installs'].unique()))
InstallsChange = {}
for i in range(0,len(InstallsVal)):
    InstallsChange[InstallsVal[i]]=i
df['Installs'] = df['Installs'].map(InstallsChange).astype(int)


# In[155]:


df.Installs.head()


# In[156]:


df.Price.unique()


# In[ ]:


df.Price=df.Price.apply(lambda x: x.replace('$',''))
df.Price=df.Price.apply(lambda x: float(x))


# In[158]:


df.Price.unique()


# In[159]:


df.Price.describe()


# In[ ]:


def Types(type):
    if type == 'Free':
        return 0
    else:
        return 1
df.Type=df.Type.map(Types)    


# In[161]:


df.Type.unique()


# In[162]:



df['Content Rating'].unique()


# In[163]:


df['Content Rating'].value_counts()


# In[164]:


graph= sns.countplot(x="Content Rating",data=df, palette = "Set1")
graph.set_xticklabels(graph.get_xticklabels(), rotation=90)
graph 


# In[ ]:


df.Reviews=df.Reviews.apply(lambda x: int(x))


# In[ ]:


CategoryVal = sorted(list(df['Category'].unique()))
Count = len(CategoryVal)
CategoryChange = {}
for i in range(0,Count):
    CategoryChange[CategoryVal[i]]=i
df["Category_int"] = df["Category"].map(CategoryChange).astype(int)   


# In[ ]:


ContentVal = sorted(list(df['Content Rating'].unique()))
ContentChange = {}
for i in range(0,len(ContentVal)):
    ContentChange[ContentVal[i]] = i
df['Content Rating'] = df['Content Rating'].map(ContentChange).astype(int)    


# In[ ]:


GenresVal = sorted(list(df['Genres'].unique()))
GenresChange = {}
for i in range(0,len(GenresVal)):
    GenresChange[GenresVal[i]]=i
df['Genres'] = df['Genres'].map(GenresChange).astype(int)


# In[ ]:


df.drop(['Last Updated','Current Ver','Android Ver','App'], axis = 1,inplace = True)


# In[170]:


df.info()


# In[171]:


df.head()


# In[172]:


corrMat = df[['Rating','Reviews','Size','Installs','Type','Price','Content Rating','Genres','Category_int']].corr()
mask = np.array(corrMat)
mask[np.tril_indices_from(mask)] = False
plt.subplots(figsize=(20,10))
plt.xticks(rotation=90)
sns.heatmap(corrMat, mask=mask,vmax=0.8, square=True,annot=True)


# In[173]:


var = ['Reviews','Size','Rating','Type','Price','Content Rating','Genres','Category_int']
for index in range(8):
    data = pd.concat([df['Installs'],df[var[index]]],axis=1)
    data.plot.scatter(x=var[index],y='Installs',ylim=(0,18),figsize=(6,4))


# In[174]:


data = pd.concat([df['Installs'],df['Rating']], axis=1)
fig = sns.boxplot(x='Rating', y="Installs", data=data)
fig.axis(ymin=0, ymax=18);


# In[175]:


from sklearn.linear_model import LinearRegression

feature_col =['Reviews','Size','Type','Rating','Price','Content Rating','Genres','Category_int']
x=df[feature_col]
y=df.Installs
print(x.shape,y.shape)


# In[176]:


from sklearn.preprocessing import MinMaxScaler
x_c = x[:]
x_trans = MinMaxScaler().fit_transform(x_c)


# In[ ]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x_trans,y,test_size = 0.3)


# In[178]:


print(x_train.shape,y_train.shape)


# In[ ]:


lm = LinearRegression()
m = lm.fit(x_train,y_train)


# In[199]:


m.score(x_test,y_test)
print ('R-square :',m.score(x_test,y_test))


# In[196]:


pred=m.predict(x_test)
print(pred)


# In[190]:


plt.scatter(y_test, pred)
plt.xlabel("True Values")
plt.ylabel("Predictions")


# In[186]:


from sklearn.model_selection import cross_val_score
scores =-cross_val_score(lm,x_train,y_train,cv=5,scoring='neg_mean_absolute_error')
print(scores)
print(np.mean(scores))

