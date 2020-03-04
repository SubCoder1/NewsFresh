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

#This is where I was figuring out how to use the classifier
def extract(link):
    article = open(link,"r")
    article = article.read()
    article = article.lower()
    article = re.sub(r'[^a-zA-Z0-9\s]', ' ', article)
    article = [article]
    return article

def train_model():

    #just using dummy data from a text
    article = extract("/home/david/2019-ca400-taland2/src/dataset/test.txt")
    dftrain = pd.read_csv('/home/david/2019-ca400-taland2/src/dataset/train.csv')
    #drops rows that have null values
    dftrain = dftrain.dropna()
    #Set column names to variables
    df_x = dftrain['text']
    df_y = dftrain['label']

    #split training data
    x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.33, random_state=53)

    # cv = CountVectorizer(stop_words = 'english', max_features = 1000)
    # x_traincv = cv.fit_transform(x_train)
    # article_testcv = cv.transform(article)

    tfv = TfidfVectorizer( stop_words = 'english',max_df = 0.7, max_features =1000)
    x_traintf = tfv.fit_transform(x_train)
    article_testtf = tfv.transform(article)
    tfv_test = tfv.transform(x_test)

    #tfv_df = pd.DataFrame(x_traintf.A, columns = tfv.get_feature_names())
    #print(tfv_df.head())

    #accuracy = 0.873

    # mnb_clf = MultinomialNB()
    # mnb_clf.fit(x_traintf, y_train)
    # pred = mnb_clf.predict(tfv_test)
    #
    #accuracy = 0.925

    pac = PassiveAggressiveClassifier(n_iter_no_change= 5, max_iter = 10, early_stopping = True)
    pac.fit(x_traintf, y_train)
    pred = pac.predict(article_testtf)
    accuracy = metrics.accuracy_score(y_test, pred)

    #pred = .predict(tfv_test)
    #pred = mnb_clf.predict(article_testtf)
    #
    # if pred == [0]:
    #     print("This news article is reliable")
    # else:
    #     print("This news article is deemed unreliable")


    print("MultinomialNB accuracy:   %0.3f" % accuracy)

    #joblib.dump(cv, 'cv.pkl')
    #joblib.dump(tfv, 'tfv.pkl')
    #joblib.dump(mnb_clf, 'mnb.pkl')
    #joblib.dump(pac, 'pac.pkl')

def main():
    train_model()

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    stop = timeit.default_timer()
    print('Time: ', stop - start)
