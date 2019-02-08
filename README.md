<h1>Welcome to Movie Recommender App!</h1>
<p>This is a simple Flask app to get movie recommendations based on three popular recommendation algorithms. The app deployed on heroku can be viewed <a href='http://anjali-movie-recommender.herokuapp.com/home'>here.</a></p>
<h2>Getting Started</h2>
Clone the repository and navigate to its directory. Set your environment variable ```FLASK_APP``` by entering:  

```
FLASK_APP=env_var.py 
```

Type ```flask run``` to run the app on localhost. Go to ```localhost:5000/home``` to access the app.
<h3>Prerequisites</h3>
<p>Python and pip are the initial requirements. The others are given in requirements.txt and can be installed once you clone the repository.</p>
<h3>Steps in creation of this project:</h3>
<ul>
<li><b>Data Acquisition:</b> The data for the movies (consisting of the following attributes: Movie Number, Movie Name, Director, Poster) was scraped from IMDB using the <a href='http://www.omdbapi.com'>OMDB API.</a>It was stored in a MongoDB database as a collection. Another collection was created in the same database to store the dummy users and ratings (which were required for the algorithms). A total of 102 movies were stored in the movie collection, and 135 entries in the dummy user collection.</li>
<li><b>Movie Recommendation System:</b>This was built by using three recommendation algorithms: user-user collaborative filtering, item-item collaborative filtering and low rank matrix factorization. Input from users is taken in the form of 5 movies and their corresponding ratings. This is converted to a Pandas dataframe and added to the MongoDB collection of users, and also included in the user-item matrix. Similarity matrices were calculated next, using Manhattan similarity criterion. Then the predicted user ratings over the entire user-item matrix (which now has the new user data as well) were calculated, and the five highest ratings for our current user were retrieved. I have ensured that the same movies already rated by the user are not repeated in the recommendations.</li>
<li><b>Creation of app:</b>The algorithms having been written, the next step was to create a Flask web app to run the same. Input was rendered using Jinja2 and HTML. Users are first shown the list of movies in the database, and asked to rate them by choosing the movie from a dropdown menu and entering the corresponding rating.</li>
<li><b>Deployment on Heroku:</b>The next step was to improve the code appearance, check its running and deploy it on Heroku. A Github repository was created as well for the app.</li></ul>

<h3>Codebase Explanation</h3>
<ul> 
  <li>```routes.py``` stores all the routes and views for the app (including the recommendation algorithms).</li>
  <li> ```forms.py``` stores all the rendered forms on the app (created using WTForms)</li>
  <li> Templates are stored in ```templates```. Given below are the template files used to render the app.
    <ul>
      <li> ```base.html``` contains the basic appearance/structure of the app.</li>
      <li> ```reco.html``` contains the HTML code to render the homepage and form data. </li>
      <li> ```results.html``` provides the results (recommendations) to the user.
    </ul>
  </li>
  <li> ```env_var.py``` is used for setting the environment variable FLASK_APP (defines application instance).</li>
  </ul>
  
  <h3>Requirements</h3>
  Given below are the packages used for building this project.
  ```
certifi==2018.11.29
chardet==3.0.4
Click==7.0
Flask==1.0.2
gunicorn==19.9.0
idna==2.8
itsdangerous==1.1.0
Jinja2==2.10
MarkupSafe==1.1.0
numpy==1.16.1
pandas==0.24.1
pymongo==3.7.2
python-dateutil==2.8.0
pytz==2018.9
requests==2.21.0
scikit-learn==0.20.2
scipy==1.2.0
flask-wtf==0.14.2
six==1.12.0
urllib3==1.24.1
Werkzeug==0.14.1
```
WTForms==2.2.1
dnspython==1.16.0
  
  


