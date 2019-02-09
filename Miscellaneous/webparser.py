from bs4 import BeautifulSoup
import json
from pandas import DataFrame
import requests
from pymongo import MongoClient
import urllib.request

url = "http://www.omdbapi.com/?apikey=50591d47&t=Ocean+Girl"


conn=MongoClient("mongodb+srv://anjalibhavan98:KLfDXoK4svurgvED@cluster0-8bw2g.mongodb.net/anjali_precog_imdb")
db=conn.anjali_precog_imdb
collection=db.imdb_movies

data = json.load(urllib.request.urlopen(url))

rec1={"name":data['Title'],
"year":data['Year'],
"poster":data['Poster'],
"director":data['Director']
}
rec_id1 = collection.insert_one(rec1)      
print("Data inserted")
cursor = collection.find() 
for record in cursor: 
    print(record)  

