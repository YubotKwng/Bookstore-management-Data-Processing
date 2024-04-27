import os
import pandas as pd
from merge import merge_func

# change on current working directory 
# os.chdir('/home/code')
print("Current Working Directory:", os.getcwd())

# Define file names
ratings_file = 'BX-Ratings.csv'
books_file = 'BX-Books.csv'
users_file = 'BX-Users.csv'
output_file = 'Final_Merged.csv'

# Read data from CSV files
ratings_file = pd.read_csv(ratings_file)
books_file = pd.read_csv(books_file)
users_file = pd.read_csv(users_file)


# calling merge function that merge base on user id, ISBN and ratings
merge_func(ratings_file, books_file, users_file)




