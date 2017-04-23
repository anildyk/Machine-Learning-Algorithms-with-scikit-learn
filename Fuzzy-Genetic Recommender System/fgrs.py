import pandas as pd
import numpy as np
from fuzzy_sets import Age, GIM
import gim

def eucledian(A,B):
    return np.linalg.norm(A-B)

def fuzzy_dist(a, b, A, B):
    return abs(a-b)*eucledian(A,B)
#print fuzzy_dist(35, 40, np.array([3, 4 ,5]), np.array([4, 5, 6]))

#Load data form MovieLens data
#Load users
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('ml-100k/u.user', sep='|', names=u_cols, encoding='latin-1')
#load ratings
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols, encoding='latin-1')
#load genres
i_cols = ['movie id', 'movie title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
 'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
items = pd.read_csv('ml-100k/u.item', sep='|', names=i_cols,
 encoding='latin-1')

#Most rated movies (497 movies having # of movies rared >= 60)
most_rated = ratings.groupby('movie_id').size().sort_values(ascending=False)[:497]  

#Extract users those have rated most_rated movies
users_top = [[]]
for i in most_rated_movies:
    users_top.append([ratings.loc[ratings['movie_id'] == i]['user_id']])
user_tops = np.array([users_top])

#Implementing fuzzy sets: class Age and GIM
#GIM = Genre Interestingness Measure
#Use young(), middle(), old() of Age class
#Use very_bad(), bad(), average(), good(), very_good(), excellent() of GIM class
a = Age()
g = GIM()
print g.very_bad(3), g.bad(3), g.average(4)
print a.young(23) a.middle(23), a.old(45)
