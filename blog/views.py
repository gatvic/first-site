from django.shortcuts import render
from django.utils import timezone
# from django.http import HttpResponse, Http404
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/base.html', {'posts': posts})


# def categories(request, catid):
#    if request.GET:
#        print(request.GET)
#    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{cat}</p>')


# def pageNotFound(request, exeption):
#    return HttpResponse
