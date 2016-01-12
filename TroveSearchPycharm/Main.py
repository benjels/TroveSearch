__author__ = 'user'
from flask import Flask
import os
import json

app = Flask(__name__)
TROVE_ARTICLES_PATH = "C:\\!2015SCHOLARSHIPSTUFF\\TroveJSON\\"
WIKIPEDIA_ARTICLES_PATH = "C:\\!2015SCHOLARSHIPSTUFF\\WikipediaJSON\\"


@app.route("/")
def home():
    return("there's nobody here")


@app.route("/trove/<troveID>")
def fetchTroveArticle(troveID):
    with open(TROVE_ARTICLES_PATH + str(troveID) + ".json") as troveJSON:
        return "<br/>".join(troveJSON.readlines())

@app.route("/wikipedia/<title>")
def fetchWikipediaInfo(title):#TODO: idk why this magicallly works regardless of upper/lower case
    with open(WIKIPEDIA_ARTICLES_PATH + title.replace(" ", "_") + ".json") as wikipediaJSON:
        return "<br/>".join(wikipediaJSON.readlines())




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("80"), debug=True)

