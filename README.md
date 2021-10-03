# Text-Data-Analysis

This is a small project based on youtube data. 
Basically, we are analysing the viewers reaction for a particular video. We are analysing text and emojis from the comment section.

Pandas is used for data manipulation, numpy for numerical computations, matplotlib and seaborn for data visualization. Wordcloud is used for generating collection of most used words in the comment section. 

Positive and negative polarity of comments has been visualized.
Also, wordcloud has been generated for tags on the videos.

Heatmap is generated for finding correlation between views, likes and dislikes.
Plotly is used to generate bar graph to show top 20 emojis used by the viewers. 

To import plotly in your project, use below commands:
  from plotly import graph_objs as go
  from plotly.offline import iplot
