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

#All in one DataFrame
df1 = pd.merge(users, ratings, on='user_id')
df = pd.merge(df1, items, on='movie_id')

#Most rated movies till movies having ratings > 60
most_rated_movies = df.groupby('movie_title').size().sort_values(ascending=False)[:497]
#Extract users those have rated most_rated movies
top_users = df.groupby('user_id').size().sort_values(ascending=False)[:497]

#select randomly -> active_users and training_users - pd.Series()
active_users = top_users.sample(frac=(50/497.0))
training_users = top_users.drop(active_users.index)
#Make feature vectors for training users 
#tu_data - DataFrame(), Get deyails of the users which are in training_users
tu_data = df.loc[df['user_id'].isin(training_users)]
#Get age of all users which are in  tu_data
tu_age = tu_data['age']
tu_ages = tu_age.drop_duplicates()
#Apply fuzzy logic to age feature.
age_columns = ['age_young', 'age_middle', 'age_old']
tu_fuzzy_ages = pd.DataFrame(columns=age_columns)
a = Age()
j=0
for i in tu_ages:
    x =  [a.young(i), a.middle(i), a.old(i)]
    tu_fuzzy_ages.loc[j] = x
    j = j+1
print tu_fuzzy_ages

#Implementing fuzzy sets: class Age and GIM
#GIM = Genre Interestingness Measure
#Use young(), middle(), old() of Age class
#Use very_bad(), bad(), average(), good(), very_good(), excellent() of GIM class
#Make an object of Age and GIM classes
g = GIM()
#Examples of Age and GIM fuzzy sets
print 'GIM Example for value gim = 3.5:', g.very_bad(3.5), g.bad(3.5), g.average(3.5), g.good(3.5), g.very_good(3.5), g.excellent(3.5) 
x = []
y = []
x =  [a.young(23), a.middle(23), a.old(23)]
y = [a.young(18), a.middle(18), a.old(18)]
print "Examples of Fuzzy sets of Age: ", x, y
#Example of fuzzy distance between two age 18 and 23 and their fuzzy sets
print "Fuzzty distance between Age 18 and 23: ", fuzzy_dist(23, 18, np.array(x), np.array(y))
