# from django.shortcuts import render
from datetime import datetime, timezone
from django.views.generic import ListView, DetailView
from .models import Post

class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['time_now'] = datetime.utcnow()
        context['time_now'] = datetime.now(timezone.utc) 
        # context['value1'] = None
        return context
    
class NewsDetail(DetailView):
    model = Post
    template_name ='news_detail.html'
    context_object_name = 'news_detail'
    
class LoremDetail(DetailView):
    model = Post
    template_name ='lorem_post.html'
    context_object_name = 'lorem_post'
