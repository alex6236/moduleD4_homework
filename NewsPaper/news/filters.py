from django_filters import FilterSet
from .models import Post

class PostFilter(FilterSet):
    
    class Meta:
        model = Post
        fields = {
            'dataCreation': ['gt'], 
            'title': ['icontains'], 
            'author__authorUser__username': ['icontains'],
        }
        # fields = ('dataCreation', 'title', 'author__authorUser__username')