from django.shortcuts import render, HttpResponse
from django.db import transaction
from django.db.models import F
from django.contrib.auth.models import User
from Dashboard.models import NewsModel, NewsVoteModel
import json, re, os, pickle
import pandas as pd
import numpy as np
from newspaper import Article

bow = pickle.load(open("./fake_news_classifier/bow.pkl", "rb"))
model = pickle.load(open("./fake_news_classifier/model.pkl", "rb"))

# Used by bow pickle file
def clean_article(article):
    art = re.sub("[^A-Za-z0-9' ]", '', str(article))
    art2 = re.sub("[( ' )(' )( ')]", ' ', str(art))
    art3 = re.sub("\s[A-Za-z]\s", ' ', str(art2))
    return art3.lower()

def classify(news_id):
    news_model_obj = NewsModel.objects.filter(news_id=news_id).first()
    news_vote_obj = news_model_obj.news_conn
    list_comment = [news_model_obj.news]

    list_comment = clean_article(list_comment)
    list_comment = [list_comment]
    vect = bow.transform(list_comment)

    vect = pd.DataFrame(vect.toarray())
    vect.columns = bow.get_feature_names()

    prediction_array = model.predict(vect)
    proba_array = model.predict_proba(vect)

    maxProba = np.amax(proba_array)
    
    total_votes = (news_vote_obj.upvote_count + news_vote_obj.downvote_count)
    vote_ratio_1, vote_ratio_2 = None, None
    if total_votes:
        if news_vote_obj.upvote_count > news_vote_obj.downvote_count:
            vote_ratio_1 = (news_vote_obj.upvote_count / total_votes) * 100
            maxProba = (maxProba + vote_ratio_1) / 2
            print(vote_ratio_1)
        else:
            vote_ratio_2 = (news_vote_obj.downvote_count / total_votes) * 100
            maxProba = (maxProba + vote_ratio_2) / 2
            print(vote_ratio_2)
    if 0 in prediction_array:
        #print("this story is real")
        news_model_obj.fake = False
    else:
        #print("this story is fake")
        news_model_obj.fake = True
                
    news_model_obj.accuracy = float(str("{0:.2f}".format(maxProba)).replace('%', ''))
    news_model_obj.save()
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
        result = None
        if activity == 'upvote':
            with transaction.atomic():
                news_model_obj = NewsModel.objects.filter(news_id=news_id).select_for_update().first()
                news_vote_obj = news_model_obj.news_conn
                news_vote_obj.upvote_count = F('upvote_count') + 1
                result = 'valid'
        elif activity == 'downvote':
            with transaction.atomic():
                news_model_obj = NewsModel.objects.filter(news_id=news_id).select_for_update().first()
                news_vote_obj = news_model_obj.news_conn
                news_vote_obj.downvote_count = F('downvote_count') + 1
                result = 'valid'
        
        news_vote_obj.save()
        news_model_obj = NewsModel.objects.filter(news_id=news_id).first()
        classify(news_id=news_model_obj.news_id)
        return HttpResponse(json.dumps(result), content_type="application/json")
    news = NewsModel.objects.select_related('news_conn')
    return render(request, 'dashboard.html', {'news':news})