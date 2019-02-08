from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import RecoForm
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances 
import json
from scipy.sparse.linalg import svds
import pandas as pd
from pandas import DataFrame
import requests
from pymongo import MongoClient
import urllib.request


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = RecoForm()
    conn = MongoClient("mongodb+srv://anjalibhavan98:KLfDXoK4svurgvED@cluster0-8bw2g.mongodb.net/anjali_precog_imdb")
    db = conn.anjali_precog_imdb
    
    #MongoDB collection of scraped IMDB movies
    collection_movies = db.imdb_movies      

    #MongoDB collection of dummy user ratings
    collection_ratings = db.dummy_ratings

    movies = DataFrame(list(collection_movies.find({})))
    movies = movies.drop(columns=['_id'])

    ratings = DataFrame(list(collection_ratings.find({})))
    ratings = ratings.drop(columns=['_id'])

    #Converting 'object' datatype to numeric for processing
    ratings['user_id'] = pd.to_numeric(ratings['user_id'])
    ratings['movie_id'] = pd.to_numeric(ratings['movie_id'])
    ratings['ratings'] = pd.to_numeric(ratings['ratings'])
    
    if form.validate_on_submit():

        unique_users, counts = np.unique(ratings.iloc[:,2], return_counts=True)
        n_users = len(counts)
        n_movies = 102
        user_item_matrix = np.zeros((n_users,n_movies))

        #Creating user-item matrix
        for line in ratings.itertuples():
            user_item_matrix[line[3]-1, line[1]] = line[2]

        #Receiving data for new user's movies and corresponding ratings
        new_user_movies=[]
        new_user_ratings=[]
        new_user_movies.append(form.movie1.data)
        new_user_ratings.append(form.ratings1.data)
        new_user_movies.extend([form.movie2.data,form.movie3.data,form.movie4.data,form.movie5.data])
        new_user_ratings.extend([form.ratings2.data,form.ratings3.data,form.ratings4.data,form.ratings5.data])

        new_user_id = str(n_users + 1)
        new_user = np.zeros((1,n_movies))
        
        #Creating dataframe of new user data to insert into our ratings MongoDB collection
        for i in range(0,5):
            new_user[0,int(new_user_movies[i])] = int(new_user_ratings[i])
            
        new_user_df = pd.DataFrame({'user_id':[new_user_id]*5,'movie_id':new_user_movies,'ratings':new_user_ratings})
        collection_ratings.insert_many(new_user_df.to_dict(orient='records'))
        
        user_item_matrix = np.vstack([user_item_matrix,new_user])

        #Calculating user-user and item-item similarities
        user_similarity = pairwise_distances(user_item_matrix,metric='manhattan')
        item_similarity = pairwise_distances(user_item_matrix.T,metric='manhattan')
        
        #Calculating matrix factors using scipy's svds algorithm. This decomposes the user-item matrix to the product of three matrices:
        #one containing user 'features', the second a diagonal matrix, and the third containing item 'features'.
        U, sigma, V = svds(user_item_matrix)
        sigma = np.diag(sigma)

        #Function to compute predictions
        def prediction(similarity, algo_type,ratings = np.zeros((n_users,n_movies)),u=0,v=0,s=0):
            if algo_type == 'item':
                pred = (ratings.dot(similarity) / np.array([np.abs(similarity).sum(axis=1)])) 
            elif algo_type == 'user':
                pred = (similarity.dot(ratings) / np.array([np.abs(similarity).sum(axis=1)]).T) 
            elif algo_type == 'matrixfac':
                pred = np.dot(np.dot(u, s), v) 
            return pred

        test_ratings = user_item_matrix
        final_preds_ii = np.zeros_like(user_item_matrix)
        final_preds_uu = np.zeros_like(user_item_matrix)
        final_preds_mf = np.zeros_like(user_item_matrix)

        final_preds_ii = prediction(similarity = item_similarity,algo_type = 'item',ratings = test_ratings)
        final_preds_uu = prediction(similarity = user_similarity,algo_type = 'user',ratings = test_ratings)
        final_preds_mf = prediction(similarity = None,algo_type = 'matrixfac',u = U,s = sigma,v = V)

        #Deleting movie-ratings that user has already submitted, so they are not repeated in the recommendations.
        final_preds_ii = np.delete(final_preds_ii,new_user_movies,axis=1)
        final_preds_uu = np.delete(final_preds_uu,new_user_movies,axis=1)
        final_preds_mf = np.delete(final_preds_mf,new_user_movies,axis=1)

        #Retrieving the indices of the top 5 recommended movies
        ind_u = np.argpartition(final_preds_uu[test_ratings.shape[0]-1,:], -5)[-5:]
        ind_i = np.argpartition(final_preds_ii[test_ratings.shape[0]-1,:], -5)[-5:]
        ind_m = np.argpartition(final_preds_mf[test_ratings.shape[0]-1,:], -5)[-5:]

        final_movies_u = []
        final_movies_i = []
        final_movies_m = []
        for i in ind_u:
            final_movies_u.append(movies.loc[i])
        for i in ind_i:
            final_movies_i.append(movies.loc[i])
        for i in ind_m:
            final_movies_m.append(movies.loc[i])

        return render_template('results.html', movies_u = final_movies_u,movies_i = final_movies_i,movies_m = final_movies_m)
    return render_template('reco.html', form = form,movielist = movies)
    
    



