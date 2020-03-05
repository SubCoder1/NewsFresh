import json
import os
import pickle
import re
from collections import namedtuple

import numpy as np
import pandas as pd
from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import F
from django.shortcuts import HttpResponse, render
from django.template.loader import render_to_string
from newspaper import Article
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Dashboard.models import NewsModel, NewsVoteModel, UserDataModel
from Dashboard.r_news_scrapper import google_search, handlelink, similarity
from Dashboard.serializers import FakeNewsAPISerializer

model = pickle.load(open('./fake_news_classifier/final_model.sav', 'rb'))
# Used by bow pickle file
def clean_article(article):
    art = re.sub("[^A-Za-z0-9' ]", '', str(article))
    art2 = re.sub("[( ' )(' )( ')]", ' ', str(art))
    art3 = re.sub("\s[A-Za-z]\s", ' ', str(art2))
    return art3.lower()

def classify(news_id):
    news_model_obj = NewsModel.objects.filter(news_id=news_id).first()
    news_vote_obj = news_model_obj.news_conn
    
    var = news_model_obj.news
    prediction_array = model.predict([var])
    prediction_array = prediction_array[0]
    maxProba = float(model.predict_proba([var])[0][1])
    print(maxProba)
    print(prediction_array)
    
    total_votes = (news_vote_obj.upvote_count + news_vote_obj.downvote_count)
    vote_ratio_1, vote_ratio_2 = None, None
    if total_votes:
        if news_vote_obj.upvote_count > news_vote_obj.downvote_count:
            vote_ratio_1 = (news_vote_obj.upvote_count / total_votes) * 100
            maxProba = (maxProba + vote_ratio_1) / 2
        else:
            vote_ratio_2 = (news_vote_obj.downvote_count / total_votes) * 100
            maxProba = (maxProba + vote_ratio_2) / 2
    if prediction_array:
        #print("this story is real")
        news_model_obj.fake = False
    else:
        #print("this story is fake")
        news_model_obj.fake = True
    
    maxProba = float(maxProba) * 100 if float(maxProba) < 1 else float(maxProba)
    news_model_obj.accuracy = float(str("{0:.2f}".format(maxProba)).replace('%', ''))
    news_model_obj.save()
    news_model_obj.refresh_from_db()
    return news_model_obj.accuracy

# Create your views here.
def DashboardView(request):
    if request.POST.get('news_link', None) is not None:
        try:
            url = request.POST['news_link']
            if not NewsModel.objects.filter(news_link=url).exists():
                article = Article(url)
                article.download()
                article.parse()
                user = User.objects.first()
                if article.text is not '':
                    news_vote_model = NewsVoteModel.objects.create()
                    news_model = NewsModel.objects.create(news_link=url, news=article.text, 
                    news_img_link=article.top_image, news_conn=news_vote_model)
                    classify(news_id=news_model.news_id)
                else:
                    print("the article could not be scraped")
            else:
                print("news already exists in db")
        except Exception as e:
            print(e)
    if request.is_ajax():
        activity = request.POST.get('activity')
        news_id = request.POST.get('news_id')
        result, vote = None, None
        if activity == 'upvote':
            with transaction.atomic():
                news_model_obj = NewsModel.objects.filter(news_id=news_id).select_for_update().first()
                news_vote_obj = news_model_obj.news_conn
                news_vote_obj.upvote_count = F('upvote_count') + 1
                result, vote = 'valid', 'upvoted'
        elif activity == 'downvote':
            with transaction.atomic():
                news_model_obj = NewsModel.objects.filter(news_id=news_id).select_for_update().first()
                news_vote_obj = news_model_obj.news_conn
                news_vote_obj.downvote_count = F('downvote_count') + 1
                result, vote = 'valid', 'downvoted'
        elif activity == 'get_related_articles':
            news_model_obj = NewsModel.objects.filter(news_id=news_id).first()
            prediction, article_title, article, url = handlelink(article_link=news_model_obj.news_link)
            #url_list, search_titles, sitename = google_search(article_title, url)
            url_list, sitename = google_search(article_title, url)
            print(url_list)
            similarity_score, avgScore = similarity(url_list, article)
            print(similarity_score)

            news = namedtuple('news', ['news_link', 'similarity_score'])
            related_news = []
            for i in range(len(url_list)):
                if '0.' not in similarity_score[i]:
                    related_news.append(news(url_list[i], round(float(similarity_score[i]))))

            return HttpResponse(json.dumps({
                'result': 'valid',
                'related_news': render_to_string('related_news.html', context={'related_news':related_news})}), 
                content_type="application/json")
        
        news_vote_obj.save()
        news_model_obj = NewsModel.objects.filter(news_id=news_id).first()
        probability = classify(news_id=news_model_obj.news_id)

        user = User.objects.first()
        user_data_obj = UserDataModel.objects.filter(user=user).first()
        user_data_obj.contribution = F('contribution') + 1

        if news_model_obj.fake and vote == 'upvoted' and user_data_obj.accuracy > 0:
            user_data_obj.accuracy = F('accuracy') - 1
            user_data_obj.currency = F('currency') - 1 if user_data_obj.currency > 1 else F('currency')
        elif not news_model_obj.fake and vote == 'downvoted' and user_data_obj.accuracy > 0:
            user_data_obj.accuracy = F('accuracy') - 1
            user_data_obj.currency = F('currency') - 1 if user_data_obj.currency > 1 else F('currency')
        else:
            user_data_obj.accuracy = F('accuracy') + 1
            user_data_obj.currency = F('currency') + 1

        user_data_obj.save()
        user_data_obj.refresh_from_db()
        user_data_obj.accuracy_perc = "{0:.2f}".format((user_data_obj.accuracy / user_data_obj.contribution) * 100)
        user_data_obj.save()
        user_data_obj.refresh_from_db()

        return HttpResponse(json.dumps({'result':result, 
        'probability':str(probability) + "%", 'contribution':user_data_obj.contribution, 
        'coins': user_data_obj.currency}),
        content_type="application/json")
        
    news = NewsModel.objects.select_related('news_conn')
    user = User.objects.first()
    user_data_obj = UserDataModel.objects.filter(user=user).first()

    return render(request, 'dashboard.html', {'news':news, 'user_data':user_data_obj})

# ------------------------- API --------------------------

@api_view(['GET'])
def process_news(request, url):
    if request.method == 'GET':
        news = NewsModel.objects.filter(news_link=str(url)).first()
        serializer = FakeNewsAPISerializer(news)
        return Response(serializer.data)