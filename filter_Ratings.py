import pandas as pd 
import re
import os 
import numpy as np

os.chdir('/home/code')
ratings_file = 'BX-Ratings.csv'

# load user data file into a dataframe 
ratings_df = pd.read_csv(ratings_file)

# convert to string to handle potential non-numeric entries
ratings_df['User-ID'] = ratings_df['User-ID'].astype(str)

def impute_missing_data(column):
    observed_values = column.dropna()
    weights = (observed_values.value_counts()/len(observed_values)).to_dict()
    missing_count = column.isnull().sum()
    imputed_values = np.random.choice(list(weights.keys()), size = missing_count, p = list(weights.values()))
    return imputed_values

def filter_userid(userid_str):
    # use regex string matching to extract numeric entries from user id strings 
    match = re.search(r'(\d+)', userid_str)
    if match:
        userid_numeric = int(match.group())
        return userid_numeric
    else:
        return pd.NA

# apply the filter_column function to the 'User-ID' column in the original dataframe
ratings_df['User-ID'] = ratings_df['User-ID'].apply(filter_userid)

# handle missing data
ratings_df.loc[ratings_df['User-ID'].isnull(), 'User-ID'] = impute_missing_data(ratings_df['User-ID'])

# convert to string to handle potential non-numeric entries
ratings_df['ISBN'] = ratings_df['ISBN'].astype(str)

def filter_ISBN(ISBN_str):
    # Use regex string matching to filter out ISBNs with the specified format
    match = re.match(r'^\d{9}[\dX]$', ISBN_str)
    return ISBN_str if match else pd.NA

# Apply the filter_isbn function to the 'ISBN' column in the original DataFrame
ratings_df['ISBN'] = ratings_df['ISBN'].apply(filter_ISBN)

# Handle missing data
ratings_df.loc[ratings_df['ISBN'].isnull(), 'ISBN'] = impute_missing_data(ratings_df['ISBN'])

# convert to string to handle potential non-numeric entries
ratings_df['Book-Rating'] = ratings_df['Book-Rating'].astype(str)

# there was no need to filter out the Book-Rating column because all entries were valid

# filter out to users who have left >=100 ratings
ratings_count = ratings_df.groupby('User-ID').size()
kjfndskfnosergjserdmgeskrldgnvob
    

print(ratings_df)

