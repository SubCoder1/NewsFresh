from newspaper import Article
import pandas as pd
import numpy as np
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
import re
from googlesearch import search
from sklearn.metrics.pairwise import cosine_similarity
from urllib.parse import urlparse

#extractor function that gets the article body from the url
def extractor(url):
    article = Article(url)
    try:
        article.download()
        article.parse()
    except:
        pass

    #gets some of the article features like title
    article_title = article.title
    article = article.text.lower()
    article = [article]
    return (article, article_title)

#function for the textbox extractor
#it doesn't need an API
def textAreaExtractor(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    text = re.sub("(\\r|\r|\n)\\n$", " ", text)
    text = [text]
    return text

#performs a google search using the article title
def google_search(title, url):
    target = url
    domain = urlparse(target).hostname
    search_title = []
    search_urls = []
    source_sites = []
    #stores the sitenames and the urls into a list
    for i in search(title, tld = "com", num = 10, start = 1, stop = 6):
        if "youtube" not in i and domain not in i:
            source_sites.append(urlparse(i).hostname)
            search_urls.append(i)
            """article = Article(i)
            try:
                article.download()
                article.parse()
            except:
                pass
            title = article.title"""

    return search_urls, source_sites

def similarity(url_list, article):
    article = article
    sim_tfv = TfidfVectorizer(stop_words ="english")
    #article needs to be vectorized first
    sim_transform1 = sim_tfv.fit_transform(article)
    cosine = []
    cosineCleaned = []
    cosineAverage = 0
    count = 0
    #loop to calculate each article from the google search
    #against the original article
    for i in url_list:
        test_article, test_title = extractor(i)
        test_article = [test_article]
        sim_transform2 = sim_tfv.transform(test_article[0])
        score = cosine_similarity(sim_transform1, sim_transform2)
        cosine.append(score*100)
        print("Article " + str(count) + " similarity calculated")
        count+=1
    for i in cosine:
        x = str(i).replace('[','').replace(']','')
        cosineCleaned.append(x)

    for i in cosine:
        if i !=0:
            cosineAverage = cosineAverage + i
        else:
            count-=1

    #averages the similarity score
    averageScore = cosineAverage/count
    averageScore = str(averageScore).replace('[','').replace(']','')
    averageScore = float(averageScore)
    print(averageScore)
    return cosineCleaned, averageScore

#classification function
def handlelink(article_link):

    #loads the  models
    job_cv = joblib.load('Dashboard/static/models/cv.pkl')
    job_pac = joblib.load('Dashboard/static/models/pac.pkl')
    job_vec = joblib.load('Dashboard/static/models/tfv.pkl')
    url = (article_link)

    #extracts the article and title from the url
    article, article_title = extractor(article_link)

    #prediction is made
    pred = job_pac.predict(job_vec.transform(article))
    print("Target article has been classified")

    return pred, article_title, article, url
    #return article_title, article, url

if __name__ == "__main__":
    #gets all the variables needed by executing the functions above
    prediction, article_title, article, url = handlelink(article_link='https://techcrunch.com/2020/03/03/smartnews-local-news-feature-now-covers-more-than-6000-u-s-cities/')
    #article_title, article, url = handlelink(article_link='https://techcrunch.com/2020/03/03/smartnews-local-news-feature-now-covers-more-than-6000-u-s-cities/')
    url_list, search_titles, sitename = google_search(article_title, url)
    print(search_titles)
    similarity_score, avgScore = similarity(url_list, article)
    