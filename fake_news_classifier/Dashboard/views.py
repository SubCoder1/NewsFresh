from django.shortcuts import render, HttpResponse
from django.db import transaction
from django.db.models import F
from Dashboard.models import NewsModel
import json

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
            # to be coded
            pass
        return HttpResponse(json.dumps(result), content_type="application/json")
    news = NewsModel.objects.select_related('news_conn')
    return render(request, 'dashboard.html', {'news':news})