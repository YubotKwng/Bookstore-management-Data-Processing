import pandas as pd 
import re
import os 

os.chdir('/home/code')
ratings_file = 'BX-Ratings.csv'

# load user data file into a dataframe 
ratings_df = pd.read_csv(ratings_file)

# convert to string to handle potential non-numeric entries
ratings_str = str(ratings_file)

def filter_userid(ratings_file):
    # use regex string matching to extract numeric entries from user id strings 
    match = re.search(r'(\d+)', ratings_str)
    if match:
        userid_numeric = int(match.group(1))
    else:
        return pd.NA

# apply the filter_column function to the 'User-ID' column in the original dataframe
ratings_df['User-ID'] = ratings_df['User-ID'].apply(filter_column)

# get rid of blank entries and leave only valid user ids
ratings_df['User-ID'] = ratings_df.dropna(subset=['User-ID'])