import csv
import pandas as pd 
import os 
import re

# change on current working directory 
# os.chdir('/home/code')

# A function that filter target list from column and save to output file
def filter_nation(users_file, column_name, target_list, output_file):
    with open(users_file, 'r', newline='') as infile, \
        open(output_file, 'w', newline='') as outfile:

        # Get column header and write to output
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()

        # Add eligible rows into output
        for row in reader:
            if row[column_name] in target_list:
                writer.writerow(row)
        

# testing
users_file = 'BX-Users.csv'
column_name = 'User-Country'
target_list = [' usa"', ' u.s. of a."', ' u.s.a."', ' united states"', ' america"', ' u.s>"', ' u.s.a>"', ' us"', ' united state"', ' united states of america"', ]
output_file = 'Filtered_Nation.csv'
filtered_rows = filter_nation(users_file, column_name, target_list, output_file)