from sklearn.externals import joblib
import re
from sklearn.feature_extraction.text import TfidfVectorizer

def extract():
    link = "/home/david/2019-ca400-taland2/src/dataset/test.txt"
    article = open(link,"r")
    article = article.read()
    article = article.lower()
    article = re.sub(r'[^a-zA-Z0-9\s]', ' ', article)
    article = [article]
    return article

def predict():
    article = extract()
    tfv = TfidfVectorizer(stop_words = 'english',max_df = 0.7, max_features =1000)
    articletest = tfv.transform(article)
    model = joblib.load('mnb_clf_joblib.pkl')
    vec = joblib.load('tfv_vec.pkl')
    model.predict(articletest)

def main():
    predict()

if __name__ == '__main__':
    main()
