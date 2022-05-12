# -*- coding: utf-8 -*-
"""
Created on Thu May 12 18:06:20 2022

@author: Augusto
"""

import pandas as pd 
import GoogleNews

# Create dictionary to store data
news_frame = {'Keyword':[], 'Header':[], 'Date':[], 'Link':[]}

# Read Excel file using pandas. Will be used to search the values inside a column
keyword_table = pd.read_csv(r'file_path\\filename.csv')  # or read_excel and .xlsx if file is in Excel format

# Reads the dataframe created previously. df[''] selects the column
for keyword in keyword_table['Column name for search']: 
    
    googlenews = GoogleNews(lang = 'pt')
    googlenews.get_news(keyword)
    news = googlenews.results()
    
    # Second loop used to extract the results as they come in nested dictionaries
    for results in news: 
        
        # Assign variables to the values
        news_header = results['title']
        news_date = results['date']
        news_link = results['link']
        
        # Append the values from GoogleNews dictionary to the table "news_frame" created previously
        news_frame['Keyword'].append(keyword)
        news_frame['Header'].append(news_header)
        news_frame['Date'].append(news_date)
        news_frame['Link'].append(news_link)      
        

# Transform the list storing values to a proper Pandas Dataframe
df_news = pd.Dataframe(news_frame) 

# Save to a file
path = 'path\\news.csv'
df_news.to_csv(path)

# Check the "headers" column for duplicates. If it exists, keeps only the last one. Useful because the date is displayed as "5 days ago" when the news is recently released
df_news.drop_duplicates(subset = 'Header', keep = 'last')
