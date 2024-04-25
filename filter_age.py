import pandas as pd 
import os 
import re

# os.chdir('/home/code')
users_file = 'BX-Users.csv'

# load user data file into a dataframe 
users_df = pd.read_csv(users_file)

def filter_age(users_file):
    
    # convert to string to handle potential non-numeric entries
    age_str=str(users_file)

    # use regex string matching to extract numeric entries from age strings 
    match = re.search(r'(\d+)', age_str)
    if match:
        age_numeric = int(match.group(1))
    else:
        return pd.NA
    
    # filter age range to 13-25
    if 13 <= age_numeric <= 25:
        return age_numeric 
    else:
        return pd.NA

# apply the filter_age function to the 'User-Age' column in the original dataframe
users_df['User-Age'] = users_df['User-Age'].apply(filter_age)

# get rid of blank entries and leave only ages in range 13-25
filtered_users_df = users_df.dropna(subset=['User-Age'])

# save filtered data to a new csv file 
filtered_users_df.to_csv("Filtered_Age.csv", index=False)


