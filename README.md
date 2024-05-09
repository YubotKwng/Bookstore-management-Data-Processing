# Eodp-2nd-Asmt
Eodp 2nd Asmt for Workshop 11 Group 9

This is a group project analyzes the behavior of highly active users at an online bookstore to enhance user engagement. By focusing on users who frequently rate books, the study identifies key patterns in demographics and preferences. We utilize data preprocessing techniques based on analytics toolkit and regex string matching, combined with k-means clustering and linear regression. The insights aim to guide the bookstore in tailoring its services to better serve its most engaged users, thereby increasing retention and driving growth.

# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Follow the steps below to set up your environment and run the necessary notebooks.

# Prerequisites
You will need Python and Jupyter Notebook or JupyterLab to run the notebooks. 

# Running the Notebooks
To successfully run the project notebooks, follow these steps:

1. Launch Jupyter Notebook or JupyterLab
    Open your command line or terminal and navigate to the project directory. Start JupyterLab or Notebook.

2. Data Preprocessing
    Before running any machine learning algorithms, you must first prepare the data. Navigate to and open the preprocessing notebooks:

    BX_preprocess_books.ipynb

    BX_preprocess_users.ipynb

    Run all the cells in this notebook to clean and prepare the data. This notebook will handle tasks like feature scaling, missing data imputation, encoding, and any other necessary data transformations. The cleaned dataframes will be exported as cleaned_books.csv and cleaned_users.csv.

3. Data Filtering
    After preprocessing the data, navigate to and open the filtering notebook:

    BX_ratings_filter.ipynb

    Run all the cells in this notebook to filter the high quality users who keeps rating more than 40 books. Then the notebooks will merge these high quality user ratings with their user and book information altogether, export in a new csv: highquality_final_merged.csv. The notebook merged original three datasets for machine training purpose and export as merge_all_original.csv.

4. Machine Learning Analysis
    After preprocessing the data, navigate to and open the machine learning notebook:

    ml_kmeans.ipynb

    ml_regresson.ipynb

    Run all the cells within this notebook to train and evaluate the models. This notebook uses the preprocessed data to fit models, and evaluate the results.

# Built With
    Python - The programming language used.

    Jupyter Notebook - Interactive computational environment.

    NumPy - Package for scientific computing.

    Pandas - Library for data manipulation and analysis.

    Scikit-Learn - Library for machine learning and statistical modeling including classification, regression, clustering, and dimensionality reduction.

    Matplotlib - Library for creating static, interactive, and animated visualizations in Python.

    Seaborn - Statistical data visualization library based on matplotlib.
    NLTK - Toolkit for natural language processing.

    VAT - Algorithm introduced from COMP20008 workshop for producing VAT heatmap.

# Authors
Alexandra Zhang 

Jiashao Chen 

Yubo Wang
