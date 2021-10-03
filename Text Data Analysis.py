#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from wordcloud import WordCloud,STOPWORDS
import re
import emoji
#import plotly.graph_objs as go
from plotly import graph_objs as go
from plotly.offline import iplot

comments = pd.read_csv(r'C:\Users\HP\Downloads\1-Youtube_Text_Data_Analysis-20210923T055249Z-001\1-Youtube_Text_Data_Analysis\GBComments.csv', error_bad_lines=False)
comments.head()
comments.isna().sum()
comments.dropna(inplace=True)

TextBlob("It's more accurate to call it the M+ (1000) be...").sentiment.polarity
polarity = []
for i in comments['comment_text']:
    polarity.append(TextBlob(i).sentiment.polarity)

comments['polarity'] = polarity
comments.head(20)
comments_positive = comments[comments['polarity'] == 1]
comments_positive.shape
comments_positive.head()

stopwords = set(STOPWORDS)
total_comments = ' '.join(comments_positive['comment_text'])
wordcloud = WordCloud(width=1000, height=500,stopwords=stopwords).generate(total_comments)

plt.figure(figsize=(15,5))
plt.imshow(wordcloud)
plt.axis('off')

comments_negative = comments[comments['polarity'] == -1]
total_comments = ' '.join(comments_negative['comment_text'])

wordcloud = WordCloud(width=1000, height=500,stopwords=stopwords).generate(total_comments)
plt.figure(figsize=(15,5))
plt.imshow(wordcloud)
plt.axis('off')

videos = pd.read_csv(r'C:\Users\HP\Downloads\1-Youtube_Text_Data_Analysis-20210923T055249Z-001\1-Youtube_Text_Data_Analysis\USvideos.csv', error_bad_lines=False)
videos.head()
tags_complete = ' '.join(videos['tags'])

tags = re.sub('[^a-zA-Z]', ' ' , tags_complete)
tags = re.sub(' +','',tags)

wordcloud=WordCloud(width=1000,height=500,stopwords=set(STOPWORDS)).generate(tags)
plt.figure(figsize=(15,5))
plt.imshow()
plt.axis('off')

sns.regplot(data=videos,x='views',y='likes')
plt.title('Regression plot for views and likes')
sns.regplot(data=videos,x='views',y='dislikes')
plt.title('Regression plot for views and dislikes')

df_corr = videos[['views','likes','dislikes']]
df_corr.corr()
sns.heatmap(df_corr.corr(),annot=True)
comments['comment_text'][1]
len(comments)
comment = comments['comment_text'][1]

[c for c in comment if c in emoji.UNICODE_EMOJI]
emoji.__version__

str = ''
for i in comments['comment_text'].dropna():
    list = [c for c in i if c in emoji.UNICODE_EMOJI]
    for ele in list:
        str = str + ele
str
result = {}
for i in set(str):
    result[i] = str.count(i)
result

final={}
for key,value in sorted(result.items(),key = lambda item:item[1]):
    final[key]=value

keys = [*final.keys()]
# [*] -> unzip operator
values = [*final.values()]

df = pd.DataFrame({'chars':keys[-20:],'num':values[-20:]})
trace = go.Bar(x = df['chars'], y = df['num'])
iplot([trace])
