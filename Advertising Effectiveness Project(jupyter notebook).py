#!/usr/bin/env python
# coding: utf-8

# # Unveiling Marketing Insights: Investigating the Relationship between Ad Investment and Sales Performance through Correlation Analysis
# 
# ## INTRODUCTION 
# 
# 
# In our quest to decode the symbiotic relationship between advertising expenditure and sales performance, we embark on a data-driven journey. Leveraging a rich dataset from Kaggle, we aim to uncover the correlation between advertising investment and sales outcomes. Our findings promise to empower businesses with actionable insights, guiding them to optimize marketing strategies, maximize returns, and propel growth in the competitive landscape of advertising and sales.
# 
# ## PURPOSE 
# 
# The purpose of this analysis is to determine the relationship between advertising spending and sales performance. By examining correlation patterns in a Kaggle dataset, our aim is to provide actionable insights for businesses to optimize their marketing strategies and improve sales outcomes.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# ### The following Python libraries are required:
# 
# - Pandas: Used for data manipulation and analysis.
# - NumPy: Essential for numerical computing and array operations.
# - Seaborn: Another data visualization library that works well with Pandas and Matplotlib, providing enhanced visualizations.
# 

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns


# 
# 
# 
# ##  DATABASE
# 
# [Kaggle_database](https://www.kaggle.com/datasets/yasserh/advertising-sales-dataset)
# click to get the data
# ![image.png](attachment:image.png)
# 

# In[7]:


df = pd.read_csv("D:\Professionaal folders\DATA SCIENCE\Machine learning\Advertising Budget and Sales.csv")
df.head()


# In[8]:


sales = df[['TV Ad Budget ($)', 'Radio Ad Budget ($)',
       'Newspaper Ad Budget ($)', 'Sales ($)']]
sales.head()


# In[9]:


sales.corr()


# Based on the correlation matrix provided, let's summarize the correlations between the advertising budgets (TV, radio, newspaper) and sales:
# 
# #### TV Ad Budget  vs. Sales :
# 
# - Correlation coefficient: 0.782
# - Summary: There is a strong positive correlation between the TV advertising budget and sales. This suggests that increasing investment in TV advertising tends to lead to higher sales.
# #### Radio Ad Budget  vs. Sales :
# 
# - Correlation coefficient: 0.576
# - Summary: There is a moderate positive correlation between the radio advertising budget and sales. Investing more in radio advertising is associated with increased sales, though the correlation is weaker compared to TV advertising.
# #### Newspaper Ad Budget  vs. Sales :
# 
# - Correlation coefficient: 0.228
# - Summary: There is a weak positive correlation between the newspaper advertising budget and sales. While there is some relationship between newspaper advertising and sales, it is the weakest among the three advertising channels.
# 
# 
# 

# # Impact of TV Advertising Budget on Sales
# 
# 

# In[20]:


sns.set(style='whitegrid')

sns.regplot(x=sales["TV Ad Budget ($)"], y=sales["Sales ($)"], scatter=True)


# #### Correlation Coefficient: 0.782224
# 
# ## Summary:
# There is a strong positive correlation (0.78) between the TV advertising budget and sales. This indicates that there is a significant influence of TV advertising expenditure on sales. As the TV advertising budget increases, there is a tendency for sales to increase as well. This suggests that allocating more budget towards TV advertising can have a substantial impact on driving sales growth.
# 
# In conclusion, the strong positive correlation between TV advertising budget and sales implies that TV advertising plays a crucial role in influencing consumer behavior and driving sales. Businesses should consider allocating a significant portion of their advertising budget towards TV advertising to maximize sales outcomes.

# # Impact of Radio Advertising Budget on Sales
# 
# 
# 
# 
# 
# 
# 
# 

# In[21]:


sns.set(style='whitegrid')

sns.regplot(x=sales["Radio Ad Budget ($)"], y=sales["Sales ($)"], scatter=True)


# #### Correlation Coefficient: 0.576223
# 
# ## Summary:
# There is a moderate positive correlation (0.58) between the radio advertising budget and sales. This indicates that there is a significant influence of radio advertising expenditure on sales. As the radio advertising budget increases, there is a tendency for sales to increase as well. This suggests that allocating more budget towards radio advertising can have a noticeable impact on driving sales growth, although not as strong as TV advertising.
# 
# In conclusion, the moderate positive correlation between radio advertising budget and sales implies that radio advertising plays a meaningful role in influencing consumer behavior and driving sales. Businesses should consider allocating a portion of their advertising budget towards radio advertising to complement their marketing efforts and maximize sales outcomes.

# # Impact of Newspaper Advertising Budget on Sales

# In[23]:


sns.set(style='whitegrid')

sns.regplot(x=sales["Newspaper Ad Budget ($)"], y=sales["Sales ($)"], scatter=True)


# #### Correlation Coefficient: 0.228299
# 
# ## Summary:
# There is a weak positive correlation (0.23) between the newspaper advertising budget and sales. This indicates that there is a modest influence of newspaper advertising expenditure on sales. While increasing the newspaper advertising budget may lead to some increase in sales, the correlation is weaker compared to TV and radio advertising.
# 
# In conclusion, the weak positive correlation between newspaper advertising budget and sales suggests that newspaper advertising may have a limited impact on driving sales compared to other advertising channels such as TV and radio. Businesses should consider allocating their advertising budget strategically, prioritizing channels with stronger correlations with sales, such as TV and radio advertising, to maximize the effectiveness of their marketing efforts and achieve better sales outcomes.
# 
# 
# 
# 
# 

# 
# 
# # Business Advice:
# 
# - Allocate a larger portion of the advertising budget towards TV advertising campaigns, as they have the highest impact on sales.
# - Consider increasing investment in radio advertising as well, as it also shows a positive correlation with sales, though to a lesser extent compared to TV.
# - Evaluate the effectiveness of newspaper advertising campaigns and consider optimizing or reallocating resources to more impactful channels if necessary.
# - Continuously monitor and analyze the performance of advertising campaigns to make data-driven decisions and maximize return on investment.
# - By following these recommendations and focusing resources on the most effective advertising channels, businesses can enhance their marketing strategies and drive greater sales outcomes.
# 
# 
# 
# 
# 
# # Conclusion:
# 
# ### The strongest correlation with sales is observed for the TV advertising budget, followed by the radio advertising budget, and then the newspaper advertising budget. This suggests that for maximizing sales, businesses should prioritize allocating their advertising budget towards TV advertising, followed by radio advertising. Newspaper advertising, while still contributing to sales, has a weaker impact compared to TV and radio.
