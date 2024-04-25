import os
from merge import merge_file
from filter_age import age_filter
from filter_nation import nationality
# change on current working directory 
# os.chdir('/home/code')
print("Current Working Directory:", os.getcwd())

# Define file names
ratings_file = 'BX-Ratings.csv'
books_file = 'BX-Books.csv'
users_file = 'BX-Users.csv'
output_file = 'Final_Merged.csv'

age_filter()

nationality()

# calling merge function that merge base on user id, ISBN and ratings
merge_file()




