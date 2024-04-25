import csv
import pandas as pd 
import os 
import re

os.chdir('COMP_208\Ass2\data')

def filter_nation(users_file, column_name, target_name, output_file):
    with open(users_file, 'r', newline='') as infile, \
        open(output_file, 'w', newline='') as outfile:

        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()

        for row in reader:
            if row[column_name] in target_name:
                writer.writerow(row)
        

# testing
users_file = 'BX-Users.csv'
column_name = 'User-Country'
target_name = [' usa"', ' u.s. of a."', ' u.s.a."', ' united states"', ' america"', ' u.s>"', ' u.s.a>"', ' us"', ' united state"', ' united states of america"', ]
output_file = 'Filtered_Nation.csv'
filtered_rows = filter_nation(users_file, column_name, target_name, output_file)