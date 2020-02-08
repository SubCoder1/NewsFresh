from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Dashboard.views import DashboardView, process_news

Dashboard = [
    path('', DashboardView, name='dashboard_view'),
    path('api/get_news/<path:url>', process_news),
]

urlpatterns = Dashboard + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)