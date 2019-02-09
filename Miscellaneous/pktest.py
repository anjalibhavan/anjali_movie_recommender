import numpy as np
from sklearn.metrics.pairwise import pairwise_distances 
import pandas as pd
from pandas import DataFrame
from scipy.sparse.linalg import svds
import requests
from pymongo import MongoClient
import urllib.request

conn = MongoClient("mongodb+srv://anjalibhavan98:KLfDXoK4svurgvED@cluster0-8bw2g.mongodb.net/anjali_precog_imdb")
db = conn.anjali_precog_imdb
collection_movies = db.imdb_movies
collection_ratings = db.dummy_ratings

movies = DataFrame(list(collection_movies.find({})))
movies = movies.drop(columns=['_id','poster'])

ratings = DataFrame(list(collection_ratings.find({})))
ratings = ratings.drop(columns=['_id'])
ratings['user_id']=pd.to_numeric(ratings['user_id'])
ratings['movie_id']=pd.to_numeric(ratings['movie_id'])
ratings['ratings']=pd.to_numeric(ratings['ratings'])

unique_users, counts = np.unique(ratings.iloc[:,2], return_counts=True)
n_users = len(counts)
print(n_users)
n_movies = 102

user_item_matrix = np.zeros((n_users,n_movies))

for line in ratings.itertuples():
    user_item_matrix[line[3]-1, line[1]] = line[2]

print('Taking input! enter 5 movie numbers first.')
new_user_movies = input().strip().split()
for i in range(0,5):
    new_user_movies[i]=int(new_user_movies[i])
print('now enter their respective ratings')
new_user_ratings = input().strip().split()
new_user_id = str(n_users + 1)


new_user = np.zeros((1,n_movies))
for i in range(0,5):
    new_user[0,int(new_user_movies[i])] = int(new_user_ratings[i])
    
new_user_df = pd.DataFrame({'user_id':[new_user_id]*5,'movie_id':new_user_movies,'ratings':new_user_ratings})
collection_ratings.insert_many(new_user_df.to_dict(orient='records'))
user_item_matrix = np.vstack([user_item_matrix,new_user])


user_similarity = pairwise_distances(user_item_matrix,metric='cosine')
item_similarity = pairwise_distances(user_item_matrix.T,metric='cosine')
U,sigma,V=svds(user_item_matrix)
sigma=np.diag(sigma)
print(U.shape)
print(V.shape)
print(sigma.shape)
print(np.dot(np.dot(U, sigma), V).shape)


def prediction(similarity, algo_type,ratings = np.zeros((n_users,n_movies)),u=0,v=0,s=0):
    if algo_type == 'item':
        pred = (ratings.dot(similarity) / np.array([np.abs(similarity).sum(axis=1)])) 
    elif algo_type == 'user':
        pred = (similarity.dot(ratings) / np.array([np.abs(similarity).sum(axis=1)]).T) 
    elif algo_type == 'matrixfac':
        pred = np.dot(np.dot(U, sigma), V) 
    return pred

test_ratings = user_item_matrix
final_preds_ii = np.zeros_like(user_item_matrix)
final_preds_uu = np.zeros_like(user_item_matrix)
final_preds_mf = np.zeros_like(user_item_matrix)

final_preds_ii = prediction(item_similarity,'item',test_ratings)
final_preds_uu = prediction(user_similarity,'user',test_ratings)
final_preds_mf = prediction(similarity=None,algo_type='matrixfac',u=U,v=V,s=sigma)


final_preds_ii = np.delete(final_preds_ii,new_user_movies,axis=1)
final_preds_uu = np.delete(final_preds_uu,new_user_movies,axis=1)
final_preds_mf = np.delete(final_preds_mf,new_user_movies,axis=1)

ind_u = np.argpartition(final_preds_uu[test_ratings.shape[0]-1,:], -5)[-5:]
ind_i = np.argpartition(final_preds_ii[test_ratings.shape[0]-1,:], -5)[-5:]
ind_m = np.argpartition(final_preds_mf[test_ratings.shape[0]-1,:], -5)[-5:]
print('Recommendations using user user collaborative filtering:')
for i in ind_u:
    print(movies.loc[i])

print('Recommendations using item item collaborative filtering:')
for i in ind_i:
    print(movies.loc[i])

print('Recommendations using user user collaborative filtering:')
for i in ind_m:
    print(movies.loc[i])
