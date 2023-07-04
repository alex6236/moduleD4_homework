# from django import views
from django.urls import path
from .views import NewsList, NewsDetail, LoremDetail, PostSearch
from . import views

urlpatterns = [
   
    path('', NewsList.as_view(), name='news'),
    path('<int:pk>/', LoremDetail.as_view(), name='lorem_post'),
    path('news/<int:pk>', NewsDetail.as_view(), name='news_detail'),
    path('search/', PostSearch.as_view(), name='search'),
    # path('search/', views.search, name='search'),
]