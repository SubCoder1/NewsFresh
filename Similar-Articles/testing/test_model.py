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
import chardet
import codecs

def extract(link):
    article = open(link,"r")
    article = article.read()
    article = article.lower()
    article = re.sub(r'[^a-zA-Z0-9\s]', ' ', article)
    article = [article]
    return article

def classify():

    job_vec = joblib.load('tfv.pkl')
    job_cv = joblib.load('cv.pkl')
    job_mnb = joblib.load('mnb.pkl')

    article = extract("/home/david/2019-ca400-taland2/src/dataset/test.txt")

    pred = job_mnb.predict(job_cv.transform(article))

    if pred == [0]:
        print("This news article is reliable")
    else:
        print("This news article is deemed unreliable")

    """
    cv = CountVectorizer(stop_words = 'english', max_features = 1000)
    article_testcv = cv.transform(article)

    tfv = TfidfVectorizer( stop_words = 'english',max_df = 0.7, max_features =1000)
    article_testtf = tfv.transform(article)

    """

def main():
    classify()

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    stop = timeit.default_timer()
    print('Time: ', stop - start)
