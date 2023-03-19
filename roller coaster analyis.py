#!/usr/bin/env python
# coding: utf-8

# # Roller Coaster

# #### Overview

# This project is slightly different than others you have encountered thus far. Instead of a step-by-step tutorial, this project contains a series of open-ended requirements which describe the project you'll be building. There are many possible ways to correctly fulfill these requirements, and you should expect to use the internet, Codecademy, and other resources when you encounter a problem that you cannot easily solve.

# #### Project Goals

# You will work to create several data visualizations that will give you insight into the world of roller coasters.

# ## Prerequisites

# In order to complete this project, you should have completed the first two lessons in the [Data Analysis with Pandas Course](https://www.codecademy.com/learn/data-processing-pandas) and the first two lessons in the [Data Visualization in Python course](https://www.codecademy.com/learn/data-visualization-python). This content is also covered in the [Data Scientist Career Path](https://www.codecademy.com/learn/paths/data-science/).

# ## Project Requirements

# 1. Roller coasters are thrilling amusement park rides designed to make you squeal and scream! They take you up high, drop you to the ground quickly, and sometimes even spin you upside down before returning to a stop. Today you will be taking control back from the roller coasters and visualizing data covering international roller coaster rankings and roller coaster statistics.
# 
#    Roller coasters are often split into two main categories based on their construction material: **wood** or **steel**. Rankings for the best wood and steel roller coasters from the 2013 to 2018 [Golden Ticket Awards](http://goldenticketawards.com) are provded in `'Golden_Ticket_Award_Winners_Wood.csv'` and `'Golden_Ticket_Award_Winners_Steel.csv'`, respectively. Load each csv into a DataFrame and inspect it to gain familiarity with the data.

# In[2]:


# 1 
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
# load rankings data
wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
# load rankings data
print(wood.head())
print(steel.head())


# 2. Write a function that will plot the ranking of a given roller coaster over time as a line. Your function should take a roller coaster's name and a ranking DataFrame as arguments. Make sure to include informative labels that describe your visualization.
# 
#    Call your function with `"El Toro"` as the roller coaster name and the wood ranking DataFrame. What issue do you notice? Update your function with an additional argument to alleviate the problem, and retest your function.

# In[3]:


# 2
# Create a function to plot rankings over time for 1 roller coaster
def plot_coaster_ranking(coaster_name,park_name,rankings_df):
    coaster_rankings = rankings_df[(rankings_df['Name'] == coaster_name) & (rankings_df['Park'] == park_name)]
    fig, ax = plt.subplots()
    ax.plot(coaster_rankings['Year of Rank'], coaster_rankings['Rank'])
    ax.set_yticks(coaster_rankings['Rank'].values)
    ax.set_xticks(coaster_rankings['Year of Rank'].values)
    ax.invert_yaxis()
    plt.title('{} Rankings'.format(coaster_name))
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.show()
    plt.close()
# Create a plot of El Toro ranking over time
plot_coaster_ranking('El Toro', 'Six Flags Great Adventure', wood)
plt.clf()


# 3. Write a function that will plot the ranking of two given roller coasters over time as lines. Your function should take both roller coasters' names and a ranking DataFrame as arguments. Make sure to include informative labels that describe your visualization.
# 
#    Call your function with `"El Toro"` as one roller coaster name, `"Boulder Dash"` as the other roller coaster name, and the wood ranking DataFrame. What issue do you notice? Update your function with two additional arguments to alleviate the problem, and retest your function.

# In[5]:


# 3
# Create a function to plot rankings over time for 2 roller coasters
def plot_2_coaster_rankings(coaster_1_name,park_1_name,coaster_2_name,park_2_name,rankings_df):
    coaster_1_rankings = rankings_df[(rankings_df['Name'] == coaster_1_name) & (rankings_df['Park'] == park_1_name)]
    coaster_2_rankings = rankings_df[(rankings_df['Name'] == coaster_2_name) & (rankings_df['Park'] == park_2_name)]
    fig, ax = plt.subplots()
    ax.plot(coaster_1_rankings['Year of Rank'], coaster_1_rankings['Rank'], color='green', label=coaster_1_name)
    ax.plot(coaster_2_rankings['Year of Rank'], coaster_2_rankings['Rank'], color='red', label=coaster_2_name)
    ax.invert_yaxis()
    plt.title('{} Rankings'.format(coaster_1_name,coaster_2_name))
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.legend()
    plt.show()
    plt.close()
# Create a plot of El Toro and Boulder Dash roller coasters
plot_2_coaster_rankings('El Toro', 'Six Flags Great Adventure', 'Boulder Dash', 'Lake Compounce', wood)
plt.clf()


# 4. Write a function that will plot the ranking of the top `n` ranked roller coasters over time as lines. Your function should take a number `n` and a ranking DataFrame as arguments. Make sure to include informative labels that describe your visualization.
# 
#    For example, if `n == 5`, your function should plot a line for each roller coaster that has a rank of `5` or lower.
#    
#    Call your function with a value of `n` and either the wood ranking or steel ranking DataFrame.

# In[6]:


# 4
# Create a function to plot top n rankings over time
def plot_top_n(rankings_df,n):
    top_n_rankings = rankings_df[rankings_df['Rank'] <= n]
    fig, ax = plt.subplots(figsize=(10,10))
    for coaster in set(top_n_rankings['Name']):
        coaster_rankings = top_n_rankings[top_n_rankings['Name'] == coaster]
        ax.plot(coaster_rankings['Year of Rank'], coaster_rankings['Rank'],label=coaster)
    ax.set_yticks([i for i in range(1,6)])
    ax.invert_yaxis()
    plt.title('Top 10 Rankings')
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.legend(loc=4)
    plt.show()
    plt.close()
# Create a plot of top n rankings over time
plot_top_n(wood,5)
plt.clf()


# 5. Now that you've visualized rankings over time, let's dive into the actual statistics of roller coasters themselves. [Captain Coaster](https://captaincoaster.com/en/) is a popular site for recording roller coaster information. Data on all roller coasters documented on Captain Coaster has been accessed through its API and stored in `roller_coasters.csv`. Load the data from the csv into a DataFrame and inspect it to gain familiarity with the data.

# In[7]:


# 5
# load roller coaster data
roller_coasters = pd.read_csv('roller_coasters.csv')
print(roller_coasters.head())


# 6. Write a function that plots a histogram of any numeric column of the roller coaster DataFrame. Your function should take a DataFrame and a column name for which a histogram should be constructed as arguments. Make sure to include informative labels that describe your visualization.
# 
#    Call your function with the roller coaster DataFrame and one of the column names.

# In[8]:


# 6
# Create a function to plot histogram of column values
def plot_histogram(coaster_df,column_name):
    plt.hist(coaster_df[column_name].dropna())
    plt.title('Histogram of Roller Coaster {}'.format(column_name))
    plt.xlabel(column_name)
    plt.ylabel('Count')
    plt.show()
    plt.close()
# Create histogram of roller coaster speed
plot_histogram(roller_coasters, 'speed')
plt.clf()
plt.close()
# Create histogram of roller coaster length
plot_histogram(roller_coasters, 'length')
plt.clf()
plt.close()
# Create histogram of roller coaster number of inversions
plot_histogram(roller_coasters, 'num_inversions')
plt.clf()
plt.close()
# Create a function to plot histogram of height values
def plot_height_histogram(coaster_df):
    heights = coaster_df[coaster_df['height'] <= 140]['height'].dropna()
    plt.hist(heights)
    plt.title('Histogram of Roller Coaster Height')
    plt.xlabel('Height')
    plt.ylabel('Count')
    plt.show()
    plt.close()
# Create a histogram of roller coaster height
plot_height_histogram(roller_coasters)
plt.clf


# 7. Write a function that creates a bar chart showing the number of inversions for each roller coaster at an amusement park. Your function should take the roller coaster DataFrame and an amusement park name as arguments. Make sure to include informative labels that describe your visualization.
# 
#    Call your function with the roller coaster DataFrame and amusement park name.

# In[10]:


# 7
# Create a function to plot inversions by coaster at park
def plot_inversions_by_coaster(coaster_df,park_name):
    park_coasters = coaster_df[coaster_df['park'] == park_name]
    park_coasters = park_coasters.sort_values('num_inversions', ascending=False)
    coaster_names = park_coasters['name']
    number_inversions = park_coasters['num_inversions']
    plt.bar(range(len(number_inversions)),number_inversions)
    ax = plt.subplot()
    ax.set_xticks(range(len(coaster_names)))
    ax.set_xticklabels(coaster_names,rotation=90)
    plt.title('Number of Inversions Per Coaster at {}'.format(park_name))
    plt.xlabel('Roller Coaster')
    plt.ylabel('# of Inversions')
    plt.show()
    plt.close()
# Create barplot of inversions by roller coasters
plot_inversions_by_coaster(roller_coasters, 'Six Flags Great Adventure')
plt.clf()


# 8. Write a function that creates a pie chart that compares the number of operating roller coasters (`'status.operating'`) to the number of closed roller coasters (`'status.closed.definitely'`). Your function should take the roller coaster DataFrame as an argument. Make sure to include informative labels that describe your visualization.
# 
#    Call your function with the roller coaster DataFrame.

# In[12]:


# 8
# Create a function to plot a pie chart of status.operating
def pie_chart_status(coaster_df):
    operating_coasters = coaster_df[coaster_df['status'] == 'status.operating']
    closed_coasters = coaster_df[coaster_df['status'] == 'status.closed.definitely']
    num_operating_coasters = len(operating_coasters)
    num_closed_coasters = len(closed_coasters)
    status_counts = [num_operating_coasters,num_closed_coasters]
    plt.pie(status_counts,autopct='%0.1f%%',labels=['Operating','Closed'])
    plt.axis('equal')
    plt.show()
    plt.close()
# Create pie chart of roller coasters
pie_chart_status(roller_coasters)
plt.clf()


# 9. `.scatter()` is another useful function in matplotlib that you might not have seen before. `.scatter()` produces a scatter plot, which is similar to `.plot()` in that it plots points on a figure. `.scatter()`, however, does not connect the points with a line. This allows you to analyze the relationship between two variables. Find [`.scatter()`'s documentation here](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html).
# 
#    Write a function that creates a scatter plot of two numeric columns of the roller coaster DataFrame. Your function should take the roller coaster DataFrame and two-column names as arguments. Make sure to include informative labels that describe your visualization.
#    
#    Call your function with the roller coaster DataFrame and two-column names.

# In[13]:


# 9
# Create a function to plot scatter of any two columns
def plot_scatter(coaster_df,column_x,column_y):
    plt.scatter(coaster_df[column_x],coaster_df[column_y])
    plt.title('Scatter Plot of {} vs. {}'.format(column_y,column_x))
    plt.xlabel(column_x)
    plt.ylabel(column_y)
    plt.show()
    plt.close()
# Create a function to plot scatter of speed vs height
def plot_scatter_height_speed(coaster_df):
    coaster_df = coaster_df[coaster_df['height'] < 140]
    plt.scatter(coaster_df['height'],coaster_df['speed'])
    plt.title('Scatter Plot Of Speed vs. Height')
    plt.xlabel('Height')
    plt.ylabel('Speed')
    plt.show()
    plt.close()
# Create a scatter plot of roller coaster height by speed
plot_scatter_height_speed(roller_coasters)
plt.clf()


# 10. Part of the fun of data analysis and visualization is digging into the data you have and answering questions that come to your mind.
# 
#     Some questions you might want to answer with the datasets provided include:
#     - What roller coaster seating type is most popular? And do different seating types result in higher/faster/longer roller coasters?
#     - Do roller coaster manufactures have any specialties (do they focus on speed, height, seating type, or inversions)?
#     - Do amusement parks have any specialties?
#     
#     What visualizations can you create that answer these questions, and any others that come to you? Share the questions you ask and the accompanying visualizations you create on the Codecademy forums.

# In[ ]:





# ## Solution

# Great work! Visit [our forums](https://discuss.codecademy.com/t/roller-coaster-challenge-project-python-pandas/462378) or the file **Roller Coaster_Solution.ipynb** to compare your project to our sample solution code. You can also learn how to host your own solution on GitHub so you can share it with other learners! Your solution might look different from ours, and that's okay! There are multiple ways to solve these projects, and you'll learn more by seeing others' code.

# In[ ]:




