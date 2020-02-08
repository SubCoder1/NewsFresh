from rest_framework import serializers
from Dashboard.models import NewsModel

# Define your serializers here
class FakeNewsAPISerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsModel
        fields = ('fake', 'accuracy',)