import pandas as pd
import re

ratings_file = 'BX-Ratings.csv'

# load user data file into a dataframe 
ratings_df = pd.read_csv(ratings_file)

# convert to string to handle potential non-numeric entries
ratings_str = str(ratings_file)

def filter_column(ratings_file):
    
    # use regex string matching to extract numeric entries from user id strings 
    match = re.search(r'(\d+)', ratings_str)
    if match:
        userid_numeric = int(match.group(1))
    else:
        return pd.NA