import pandas as pd 
import csv
import re

users_file = 'BX-Users.csv'

# load user data file into a dataframe 
users_df = pd.read_csv(users_file)

# City filter function
# Delete rows that do not start with a letter
def filter_city(users_df):
    # Delete rows that contain missing values
    users_df.dropna(subset=['User-City'], inplace=True)
    users_df = users_df[users_df['User-City'].str.match(r"^[a-zA-Z().\-/'']+$")]
    return users_df

# State filter function
# Delete rows with length < 4
def filter_state(users_df):
    users_df = users_df[users_df['User-State'].str.len() >= 4]
    return users_df

# Country filter function
# Only USA-related rows are reserved
def filter_nation(users_df):
    target_list = [' usa"', ' u.s. of a."', ' u.s.a."', ' united states"', ' america"', ' u.s>"', ' u.s.a>"', ' us"', ' united state"', ' united states of america"']
    users_df = users_df[users_df['User-Country'].isin(target_list)]
    return users_df

# Age filter function
# Delete data over 100 years old
def filter_age(users_df):
    # Converts User-Age columns to numeric types
    users_df['User-Age'] = pd.to_numeric(users_df['User-Age'], errors='coerce')
    # Delete rows that contain missing values
    users_df.dropna(subset=['User-Age'], inplace=True)
    users_df = users_df[users_df['User-Age'] <= 100]
    return users_df

# Overall function
def filter_user(users_df):
    users_df = filter_city(users_df)
    users_df = filter_state(users_df)
    users_df = filter_nation(users_df)
    users_df = filter_age(users_df)
    output_file = 'Filtered_Users.csv'
    users_df.to_csv(output_file, index=False)


filter_user(users_df)
