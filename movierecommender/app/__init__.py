from flask import Flask
from config import Config
#from flask_thumbnails import Thumbnail

app = Flask(__name__)
app.config.from_object(Config)


from app import routes

