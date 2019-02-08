<h1>Welcome to Movie Recommender App!</h1>
<p>This is a simple Flask app to get movie recommendations based on three popular recommendation algorithms. The app deployed on heroku can be viewed <a href='http://anjali-movie-recommender.herokuapp.com/'>here.</a></p>
<h2>Getting Started</h2>
Clone the repository and navigate to its directory. Set your environment variable ```FLASK_APP``` by entering:  

```
FLASK_APP=env_var.py 
```

Type ```flask run``` to run the app on localhost. Go to ```localhost:5000/home``` to access the app.
<h3>Prerequisites</h3>
<p>Python and pip are the initial requirements. The others are given in requirements.txt and can be installed once you clone the repository.</p>
<h3>Steps in creation of this project:</h3>
<li><b>Database creation:</b> The data for the movies (consisting of the following attributes: Movie Number, Movie Name, Director, Poster) was scraped from IMDB using the <a href='http://www.omdbapi.com'>OMDB API.</a>It was stored in a MongoDB database as a collection. Another collection was created in the same database to store the dummy users and ratings (which were required for the algorithms). A total of 102 movies were stored in the movie collection, and 135 entries in the dummy user collection.</li>
<li></li>


