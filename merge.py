import pandas as pd

ratings_df = pd.read_csv('BX-Ratings.csv')
books_df = pd.read_csv('BX-Books.csv')
users_df = pd.read_csv('BX-Users.csv')

def merge_rating_book(ratings_df, books_df):
    
    # First merge: Ratings with Books on 'ISBN'
    ratings_books_merged = pd.merge(ratings_df, books_df, on='ISBN', how='inner')

    # Save the merged DataFrame to a new CSV file
    ratings_books_merged.to_csv('rate_andbook.csv', index=False)

merge_rating_book(ratings_df, books_df)

def merge_all(ratings_df, books_df, users_df):
    # First merge: Ratings with Books on 'ISBN'
    ratings_books_merged = pd.merge(ratings_df, books_df, on='ISBN', how='inner')

    # Second merge: Resulting DataFrame with Users on 'User-ID'
    final_merged_df = pd.merge(ratings_books_merged, users_df, on='User-ID', how='inner')

    # Save the merged DataFrame to a new CSV file
    final_merged_df.to_csv('final_merge.csv', index=False)

merge_all(ratings_df, books_df, users_df)

