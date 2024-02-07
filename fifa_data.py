import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
fifa = pd.read_csv(r"C:\Users\ayush\Downloads\england-premier-league-players-2018-to-2019-stats.csv", encoding = 'unicode_escape')

fifa
fifa.info()
fifa.head()
fifa.columns
fifa.rename(columns={'minutes_played_overall':'Total_min'},inplace=True)
fifa.rename(columns={'minutes_played_home':'min_at_home'},inplace= True)
fifa.columns



sns.set(rc={'figure.figsize':(10,100)})
age_grp = sns.countplot(data = fifa,y='Total_min')
for bars in age_grp.containers:
    age_grp.bar_label(bars)
    
#from this information we can conclude the number of players who have played a certain amount of time limit.



sns.set(rc={'figure.figsize':(10,5)})
age_grp = sns.countplot(data = fifa,x='age')
for bars in age_grp.containers:
    age_grp.bar_label(bars)
    
#from this information we can conclude that maximum active football players are from the age group of 25-33
The number of youngesters are far more than the number of aged players or players who are close towards retirement.




sns.set(rc={'figure.figsize':(10,100)})
age_grp = sns.countplot(data = fifa,y='Total_min',hue = 'position')
for bars in age_grp.containers:
    age_grp.bar_label(bars)
    
#from the plotting graph we can say that players who have played the most minutes for a team are mostly goalkeepers which is followed by midfielders and then defenders.




sns.set(rc={'figure.figsize':(10,5)})
age_grp = sns.countplot(data = fifa,x='age',hue='position')
for bars in age_grp.containers:
    age_grp.bar_label(bars)

#from the plotted graph we can say that in every age group the maximum number of players promoted are midfielders which are closely followed by defenders.





age_time_player = fifa.groupby(['age'], as_index=False)['Total_min'].sum().sort_values(by='Total_min', ascending=True)

sns.set(rc={'figure.figsize':(10,15)})
sns.barplot(data = sales_state, x = 'age',y= 'Total_min')
#
#from the given graph we can conclude that player with an age around 30 is being given the most amount of playing time. Therefore we can say that a player will most certainly hit his prime between the age of 27 to 32.







sns.set(rc={'figure.figsize':(20,250)})
age_grp = sns.countplot(data = fifa,x='min_at_home',hue = 'position')
for bars in age_grp.containers:
    age_grp.bar_label(bars)
# from this graph we can conclude that the maximum players between the age of 21 to 25 are being given the maximum home game time. Therefore we can say that young players are being avoided to be played in the away games because of the inexperience and immaturity.   