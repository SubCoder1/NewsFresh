from bs4 import BeautifulSoup
from newspaper import Article
import json
import pickle
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

def load_model(url):
    article = Article(url)
    article.download()
    article.parse()
    var = str(article.text)

    model = pickle.load(open('final_model.sav', 'rb'))
    prediction = model.predict([var])
    prob = model.predict_proba([var])
    return [prediction[0], prob[0][1]]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        url = request.form['url']
        result = load_model(url)
        return render_template("final_result.html", result=result)


if __name__ == '__main__':
    
    print("Model Loaded")
    app.run(debug=True)
