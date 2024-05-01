import pandas as pd

# Define file names
#ratings_file = 'BX-Ratings.csv'
# Using cleadned books instead
#books_file = 'cleaned_Books.csv'
#users_file = 'BX-Users.csv'

# Read data from CSV files
#ratings_df = pd.read_csv(ratings_file)
#books_df = pd.read_csv(books_file)

def merge_rating(ratings_df, books_df):
    # First merge: Ratings with Books on 'ISBN'
    ratings_books_merged = pd.merge(ratings_df, books_df, on='ISBN', how='inner')

    # Save the merged DataFrame to a new CSV file
    ratings_books_merged.to_csv('rating_withbooks.csv', index=False)

merge_rating(ratings_df, books_df)

def merge_users(ratings_df, books_df, users_df):
    # First merge: Ratings with Books on 'ISBN'
    ratings_books_merged = pd.merge(ratings_df, books_df, on='ISBN', how='inner')

    # Second merge: Resulting DataFrame with Users on 'User-ID'
    final_merged_df = pd.merge(ratings_books_merged, users_df, on='User-ID', how='inner')

    # Save the merged DataFrame to a new CSV file
    final_merged_df.to_csv('final_merge.csv', index=False)

merge_users(ratings_df, books_df, users_df)

