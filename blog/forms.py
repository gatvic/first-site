from django.forms import ModelForm

from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'slug', 'title',
                  'text', 'published_date', 'cat')
