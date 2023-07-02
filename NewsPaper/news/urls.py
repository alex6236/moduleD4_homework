from django.urls import path
from .views import NewsList, NewsDetail, LoremDetail, PostSearch

urlpatterns = [
    path('', NewsList.as_view(), name='news'),
    path('news/<int:pk>/', LoremDetail.as_view(), name='lorem_post'),
    path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
    path('search/', PostSearch.as_view(), name='search')
]