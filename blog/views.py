from django.shortcuts import render
# , get_list_or_404
# from django.utils import timezone
# from django.http import HttpResponse
# , Http404
from .models import Post, Cat


def post_list(request):
    posts = Post.objects.all()
    cats = Cat.objects.all()
    context = {'posts': posts, 'cats': cats}
    return render(request, 'blog/base.html', context)


# def post_detail(request, pk):
#    post = get_list_or_404(Post, pk=pk)
#    return render(request, 'blog/post_detail.html', {'post': post})


def by_cat(request, cat_id):
    posts = Post.objects.filter(cat=cat_id)
    cats = Cat.objects.all()
    current_cat = Cat.objects.get(pk=cat_id)
    context = {'posts': posts, 'cats': cats, 'current_cat': current_cat}
    return render(request, 'blog/by_cats.html', context)
