import pandas as pd
import os

# change on current working directory 
# os.chdir('/home/code')
print("Current Working Directory:", os.getcwd())


# Define file names
ratings_file = 'BX-Ratings.csv'
books_file = 'BX-Books.csv'
users_file = 'BX-Users.csv'
output_file = 'Final_Merged.csv'

# Read data from CSV files
ratings_df = pd.read_csv(ratings_file)
books_df = pd.read_csv(books_file)
users_df = pd.read_csv(users_file)

def merge_func (ratings_file, books_file, users_file):
    # First merge: Ratings with Books on 'ISBN'
    ratings_books_merged = pd.merge(ratings_df, books_df, on='ISBN', how='inner')

    # Second merge: Resulting DataFrame with Users on 'User-ID'
    final_merged_df = pd.merge(ratings_books_merged, users_df, on='User-ID', how='inner')

    # Save the merged DataFrame to a new CSV file
    final_merged_df.to_csv(output_file, index=False)



