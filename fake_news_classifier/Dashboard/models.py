from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class NewsVoteModel(models.Model):
    upvote = models.ManyToManyField(User, related_name='upvoted_news')
    upvote_count = models.IntegerField(default=0)
    downvote = models.ManyToManyField(User, related_name='downvoted_news')
    downvote_count = models.IntegerField(default=0)
    objects = models.Manager()

    def __str__(self):
        return f"upvote: {self.upvote_count}, downvote: {self.downvote_count}"

class NewsModel(models.Model):
    news_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    news = models.TextField(unique=True, blank=False, default='')
    news_link = models.TextField(blank=False)
    news_img_link = models.TextField(blank=True)
    fake = models.BooleanField(default=False)
    accuracy = models.FloatField(default=0.00)
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='news_posted')
    news_conn = models.OneToOneField(NewsVoteModel, on_delete=models.CASCADE, default=1, related_name='news_model')
    objects = models.Manager()

    class Meta:
        ordering = ['-date_time']

    def __str__(self):
        return self.user.username + " " + str(self.date_time)

class UserDataModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_details")
    accuracy = models.IntegerField(default=0)
    currency = models.IntegerField(default=1)
    accuracy_perc = models.FloatField(default=0.00)
    contribution = models.IntegerField(default=0)
    objects = models.Manager()

    def __str__(self):
        return str(self.user.username) + " DataModel"