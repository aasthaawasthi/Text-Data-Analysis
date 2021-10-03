#!/usr/bin/env python
# coding: utf-8

# In[14]:


# pandas is used for data manipulation
import pandas as pd

# numpy is used for numerical computations on data
import numpy as np

# matplotlib is used for data visualization
import matplotlib.pyplot as plt

# seaborn is used for better visualization
import seaborn as sns


# In[15]:


comments = pd.read_csv(r'C:\Users\HP\Downloads\1-Youtube_Text_Data_Analysis-20210923T055249Z-001\1-Youtube_Text_Data_Analysis\GBComments.csv', error_bad_lines=False)


# In[16]:


comments.head()


# In[17]:


from textblob import TextBlob


# In[18]:


TextBlob("It's more accurate to call it the M+ (1000) be...").sentiment.polarity


# In[19]:


comments.isna().sum()


# In[20]:


comments.dropna(inplace=True)


# In[21]:


polarity = []
for i in comments['comment_text']:
    polarity.append(TextBlob(i).sentiment.polarity)


# In[22]:


comments['polarity'] = polarity


# In[23]:


comments.head(20)


# In[24]:


comments_positive = comments[comments['polarity'] == 1]


# In[25]:


comments_positive.shape


# In[26]:


comments_positive.head()


# In[27]:


from wordcloud import WordCloud,STOPWORDS


# In[28]:


stopwords = set(STOPWORDS)


# In[29]:


total_comments = ' '.join(comments_positive['comment_text'])


# In[30]:


wordcloud = WordCloud(width=1000, height=500,stopwords=stopwords).generate(total_comments)


# In[31]:


plt.figure(figsize=(15,5))
plt.imshow(wordcloud)
plt.axis('off')


# In[32]:


comments_negative = comments[comments['polarity'] == -1]


# In[33]:


total_comments = ' '.join(comments_negative['comment_text'])


# In[34]:


wordcloud = WordCloud(width=1000, height=500,stopwords=stopwords).generate(total_comments)


# In[35]:


plt.figure(figsize=(15,5))
plt.imshow(wordcloud)
plt.axis('off')


# In[36]:


videos = pd.read_csv(r'C:\Users\HP\Downloads\1-Youtube_Text_Data_Analysis-20210923T055249Z-001\1-Youtube_Text_Data_Analysis\USvideos.csv', error_bad_lines=False)


# In[37]:


videos.head()


# In[38]:


tags_complete = ' '.join(videos['tags'])


# In[39]:


import re


# In[40]:


tags = re.sub('[^a-zA-Z]', ' ' , tags_complete)


# In[41]:


tags = re.sub(' +','',tags)


# In[42]:


wordcloud=WordCloud(width=1000,height=500,stopwords=set(STOPWORDS)).generate(tags)


# In[29]:


plt.figure(figsize=(15,5))
plt.imshow()
plt.axis('off')


# In[30]:


sns.regplot(data=videos,x='views',y='likes')
plt.title('Regression plot for views and likes')


# In[31]:


sns.regplot(data=videos,x='views',y='dislikes')
plt.title('Regression plot for views and dislikes')


# In[32]:


df_corr = videos[['views','likes','dislikes']]


# In[33]:


df_corr.corr()


# In[34]:


sns.heatmap(df_corr.corr(),annot=True)


# In[35]:


comments['comment_text'][1]


# In[36]:


print('\U0001F600')


# In[37]:


import emoji


# In[38]:


len(comments)


# In[39]:


comment = comments['comment_text'][1]


# In[40]:


[c for c in comment if c in emoji.UNICODE_EMOJI]


# In[41]:


emoji.__version__


# In[42]:


str = ''
for i in comments['comment_text'].dropna():
    list = [c for c in i if c in emoji.UNICODE_EMOJI]
    for ele in list:
        str = str + ele


# In[43]:


len(str)


# In[44]:


str


# In[45]:


result = {}
for i in set(str):
    result[i] = str.count(i)


# In[46]:


result


# In[47]:


final={}
for key,value in sorted(result.items(),key = lambda item:item[1]):
    final[key]=value


# In[48]:


final


# In[49]:


keys = [*final.keys()]
# [*] -> unzip operator


# In[50]:


keys


# In[51]:


values = [*final.values()]


# In[52]:


values


# In[53]:


df = pd.DataFrame({'chars':keys[-20:],'num':values[-20:]})


# In[54]:


df


# In[55]:


#import plotly.graph_obs as go
from plotly import graph_objs as go
from plotly.offline import iplot


# In[56]:


trace = go.Bar(x = df['chars'], y = df['num'])
iplot([trace])


# In[ ]:




