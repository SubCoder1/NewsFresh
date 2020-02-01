from django.shortcuts import render
from Dashboard.models import NewsModel

# Create your views here.
def DashboardView(request):
    news = NewsModel.objects.select_related('news_conn')
    return render(request, 'dashboard.html', {'news':news})