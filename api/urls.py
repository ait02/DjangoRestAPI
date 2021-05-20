from django.urls import path, include
from .views import article_list, article_details

urlpatterns = [
    path('articles/', article_list),
    path('articles/<str:slug>/', article_details),
]
