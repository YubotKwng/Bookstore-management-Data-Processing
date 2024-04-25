import csv
import pandas as pd 
import os 
import re

# os.chdir('/home/code')

def filter_nation(users_file, column_name, target_name, output_file):
    # load user data file into a dataframe 
    # with open(usesr_file, 'r', newline=''):
    #     users = csc.read_csv(users_file)
    #     # Add rows that match the requirements
    #     filtered_rows = []
    #     for user in users:
    #         if row[column_name] == target_name:
    #             filter_rows.append(row)

    # Maybe I need to return a filtered file instead of list?
    # Waiting for new code
    with open(users_file, 'r', newline='') as infile, \
        open(output_file, 'w', newline='') as outfile:

        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()

        for row in reader:
            if row[column_name] == target_name:
                writer.writerow(row)

# testing
users_file = 'BX-Users.csv'
column_name = 'User-Country'
target_name = 'usa'
output_file = 'Filtered_Nation.csv'
filtered_rows = filter_nation(users_file, column_name, target_name, output_file)

