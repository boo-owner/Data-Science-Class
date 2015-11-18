'''
Pandas Homework with IMDb data
'''

'''
BASIC LEVEL
'''

import pandas as pd
import matplotlib.pyplot as plt

# read in 'imdb_1000.csv' and store it in a DataFrame named movies
file_path_movies = '/Users/TeddyandAlex/Documents/data_science/GA-SEA-DAT1/data/'
movies1 = file_path_movies + 'imdb_1000.csv'
movies = pd.read_csv(movies1)
# check the number of rows and columns
print movies.shape

# check the data type of each column
movies.dtypes

# calculate the average movie duration
movies.duration.mean()

# sort the DataFrame by duration to find the shortest and longest movies
movies.sort('duration')
print movies.duration.head()
print movies.duration.tail()


# create a histogram of duration, choosing an "appropriate" number of bins

movies.duration.plot(kind='hist', bins=20, title='histogram of movie duration')

# use a box plot to display that same data
movies.duration.plot(kind='box', title='box plot of movie duration')

'''
INTERMEDIATE LEVEL
'''

# count how many movies have each of the content ratings
movies.content_rating.value_counts()

# use a visualization to display that same data, including a title and x and y labels

movies.content_rating.value_counts().plot(kind='bar')


# convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP

list = ["NOT RATED", "APPROVED", "PASSED", "GP"]
for X in list:
    movies.content_rating.replace(X, "UNRATED", inplace=True)
# convert the following content ratings to "NC-17": X, TV-MA
list = ["X", "TV-MA"]
for X in list:
    movies.content_rating.replace(X, "UNRATED", inplace=True)
# count the number of missing values in each column
movies.isnull().sum()      

# if there are missing values: examine them, then fill them in with "reasonable" values
movies[movies.content_rating.isnull()]
movies.content_rating.fillna(value="PG", inplace=True)
# calculate the average star rating for movies 2 hours or longer,
# and compare that with the average star rating for movies shorter than 2 hours
movies[movies.duration>=120].star_rating.mean()
movies[movies.duration<120].star_rating.mean()

# use a visualization to detect whether there is a relationship between duration and star rating
movies.plot(kind="scatter", x='duration', y='star_rating')

# calculate the average duration for each genre
movies.groupby('genre').duration.mean()

'''
ADVANCED LEVEL
'''

# visualize the relationship between content rating and duration
movies.groupby('genre').duration.mean().plot(kind="barh")

# determine the top rated movie (by star rating) for each genre
top =  movies.groupby(['genre'])['star_rating'].idxmax()
movies.loc[top,['genre','star_rating','title' ]]


# check if there are multiple movies with the same title, and if so, determine if they are actually duplicates
movies[movies.duplicated(['title'], take_last=False)]
movies[movies.duplicated(['title'], take_last=True)]

frame[frame.duplicated(['key1','key2'],keep=False)]
dupmovies = movies[movies.duplicated('title', ) == True]
print dupmovies

#movies.set_index('title').index.get_duplicates()
# calculate the average star rating for each genre, but only include genres with at least 10 movies
#all genres

for group, df in movies.groupby(['genre']):
    if df['genre'].count() >10:
        print group
        print df.star_rating.mean()
        


'''
BONUS
'''

# Figure out something "interesting" using the actors data!
