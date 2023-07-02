# from django.shortcuts import render
from datetime import datetime, timezone
from django.views.generic import ListView, DetailView
from .models import Post
from .filters import PostFilter
from .forms import DateFilterForm, TitleFilterForm, UsernameFilterForm

class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now(timezone.utc) 
        return context
    
class NewsDetail(DetailView):
    model = Post
    template_name ='news_detail.html'
    context_object_name = 'news_detail'
    
class LoremDetail(DetailView):
    model = Post
    template_name ='lorem_post.html'
    context_object_name = 'lorem_post'

class PostSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'search'
    queryset = Post.objects.order_by('-id')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filter = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['filter'] = filter
        # context['form'] = filter.form
        context['date'] = DateFilterForm(self.request.GET or None) 
        context['title'] = TitleFilterForm(self.request.GET or None) 
        context['username'] = UsernameFilterForm(self.request.GET or None) 
        return context
