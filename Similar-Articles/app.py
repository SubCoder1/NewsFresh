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
from sklearn.model_selection import train_test_split
import re
from googlesearch import search
from sklearn.metrics.pairwise import cosine_similarity
from urllib.parse import urlparse
import re

app = Flask (__name__)
Bootstrap(app)

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
            article = Article(i)
            try:
                article.download()
                article.parse()
            except:
                pass
            title = article.title
            search_title.append(title)

    return search_urls, search_title, source_sites

#function to calculate the similarity of an article against another article
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
def handlelink():

    #loads the  models
    job_cv = joblib.load('models/cv.pkl')
    job_pac = joblib.load('models/pac.pkl')
    job_vec = joblib.load('models/tfv.pkl')
    url = (request.form['article_link'])

    #extracts the article and title from the url
    article, article_title = extractor(url)

    #prediction is made
    pred = job_pac.predict(job_vec.transform(article))
    print("Target article has been classified")

    return pred, article_title, article, url

#function to handle the body of text of the article
#this is from the bigger text box
#it doesn't need to extract anything because there's no link
def handletext():
    job_vec = joblib.load('models/tfv.pkl')
    job_pac = joblib.load('pac.pkl')
    text = request.form['article_text']
    textarticle = textAreaExtractor(text)
    pred = job_pac.predict(job_vec.transform(textarticle))

    return pred, textarticle

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/textResult', methods = ['POST'])
def textResult():
    prediction, article = handletext()
    #in case of reliable prediction
    if prediction == [0]:
        return render_template('/textresult.html', variable="This body of article has been classified as reliable",articletext = article)
    #case of unreliable prediction
    else:
        return render_template('/textresult.html', variable="This body of article has been classified as unreliable", articletext = article)

#this function handles the prediction results of the classification
#I created different categories of "support" from other articles
#with the different similarity score thresholds
@app.route('/linkResult', methods = ['POST'])
def linkResult():

    #gets all the variables needed by executing the functions above
    prediction, article_title, article, url = handlelink()
    url_list, search_titles, sitename = google_search(article_title, url)
    similarity_score, avgScore = similarity(url_list, article)

    if prediction == [0] and avgScore < 20:
        return render_template('/linkresult.html', variable = "This news article has been classified as reliable but doesn't have many articles to support this statement.", title = article_title, list = url_list, search_t = search_titles,  average = avgScore,sim_score = similarity_score, site = sitename)

    if prediction == [0] and (avgScore > 20 and avgScore < 50) :
        return render_template('/linkresult.html', variable = "This news article has been classified as reliable and is supported by some articles", title = article_title, list = url_list, search_t = search_titles,  average = avgScore,sim_score = similarity_score, site = sitename)

    if prediction == [0] and avgScore > 50 :
        return render_template('/linkresult.html', variable = "This news article has been classified as reliable and is supported by multiple articles", title = article_title, list = url_list, search_t = search_titles,  average = avgScore,sim_score = similarity_score, site = sitename)

    if prediction == [1] and avgScore < 20:
        return render_template('/linkresult.html', variable = "This news article has been classified as unreliable and doesn't have other articles talking about the same thing.", title = article_title, list = url_list, search_t = search_titles,  average = avgScore, sim_score = similarity_score, site = sitename)

    if prediction == [1] and (avgScore > 20 and avgScore < 50):
        return render_template('/linkresult.html', variable = "This news article has been classified as unreliable but may have some articles that talk about the same thing.", title = article_title, list = url_list, search_t = search_titles,  average = avgScore, sim_score = similarity_score, site = sitename)

    if prediction == [1] and avgScore > 50:
        return render_template('/linkresult.html', variable = "This news article has been classified as unreliable but have multiple articles that say the same thing.", title = article_title, list = url_list, search_t = search_titles,  average = avgScore,sim_score = similarity_score, site = sitename)

if __name__ == '__main__':
    app.run(debug = True)
