from flask import Flask,render_template,url_for,request
from flask_bootstrap import Bootstrap
from newspaper import Article
import pandas as pd
import numpy as np
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics
from collections import Counter
import timeit
import re
from googlesearch import search
from sklearn.metrics.pairwise import cosine_similarity
import pprint

#This is where I was testing and figuring out how to calculate the similarity score

def extractor(url):
    article = Article(url)
    article.download()
    article.parse()
    article_title = article.title
    article = article.text.lower()
    article = re.sub(r'[^a-zA-Z0-9\s]', ' ', article)
    article = [article]
    return (article, article_title)

def google_search(title):
    query = title
    search_dict = {}
    search_result = []
    search_title = []
    #grabs the search result from google
    for i in search(query, tld = "com", num = 10, start = 1, stop = 5):
        article = Article(i)
        article.download()
        article.parse()
        title = article.title
        search_result.append(i)
    return search_result

def similar():
    #gets the body of the target article and the title
    article, article_title = extractor("http://waterfordwhispersnews.com/2019/04/09/googling-cancer-now-the-number-one-cause-of-cancer/")

    print(article_title)
    #calls the google search function
    sites = google_search(article_title)

    #prep
    sim_tfv = TfidfVectorizer(stop_words = "english")
    #fittransform target article
    sim_transform1 = sim_tfv.fit_transform(article)
    pprint.pprint(sites)

    for i in sites:
        #returns a list
        test_article, test_title = extractor(i)
        test_article = [test_article]
        #fittransform the search result articles
        print(test_article[0])
        sim_transform2 = sim_tfv.transform(test_article[0])
        cosine = cosine_similarity(sim_transform1, sim_transform2)
        pprint.pprint(cosine)

def main():
    similar()

if __name__ == '__main__':
    main()
