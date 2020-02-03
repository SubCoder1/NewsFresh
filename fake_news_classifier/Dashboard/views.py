from django.shortcuts import render, HttpResponse
from django.db import transaction
from django.db.models import F
from Dashboard.models import NewsModel
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

# Create your views here.
def DashboardView(request):
    if request.is_ajax():
        activity = request.POST.get('activity')
        news_id = request.POST.get('news_id')
        result = None
        if activity == 'upvote':
            with transaction.atomic():
                news_model_obj = NewsModel.objects.filter(news_id=news_id).select_for_update().first()
                news_vote_obj = news_model_obj.news_conn
                news_vote_obj.upvote_count = F('upvote_count') + 1
                news_vote_obj.save()
                result = 'valid'
        elif activity == 'downvote':
            with transaction.atomic():
                news_model_obj = NewsModel.objects.filter(news_id=news_id).select_for_update().first()
                news_vote_obj = news_model_obj.news_conn
                news_vote_obj.downvote_count = F('downvote_count') + 1
                news_vote_obj.save()
                result = 'valid'

            news_model_obj = NewsModel.objects.filter(news_id=news_id).first()
            news_vote_obj = news_model_obj.news_conn
            if news_vote_obj.downvote_count > 3:
                list_comment = [news_model_obj.news]

                list_comment = clean_article(list_comment)
                list_comment = [list_comment]
                vect = bow.transform(list_comment)

                vect = pd.DataFrame(vect.toarray())
                vect.columns = bow.get_feature_names()

                prediction_array = model.predict(vect)
                proba_array = model.predict_proba(vect)

                maxProba = np.amax(proba_array)
                maxProba = format(maxProba, ".2%")

                print(maxProba)
                if 0 in prediction_array:
                    print("this story is real")
                    news_model_obj.fake = False
                else:
                    print("this story is fake")
                    news_model_obj.fake = True
                news_model_obj.save()
        return HttpResponse(json.dumps(result), content_type="application/json")
    news = NewsModel.objects.select_related('news_conn')
    return render(request, 'dashboard.html', {'news':news})