from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NewsModel(models.Model):
    news = models.TextField(unique=True, blank=False)
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1, related_name='news_posted')

class NewsVoteModel(models.Model):
    news_conn = models.OneToOneField(NewsModel, on_delete=models.CASCADE, default=1, related_name='news_model')
    upvote = models.ManyToManyField(User, related_name='upvoted_news')
    upvote_count = models.IntegerField(default=0)
    downvote = models.ManyToManyField(User, related_name='downvoted_news')
    downvote_count = models.IntegerField(default=0)