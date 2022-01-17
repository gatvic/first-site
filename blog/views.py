from django.shortcuts import render, get_list_or_404
# from django.utils import timezone
# from django.http import HttpResponse, Http404
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_list_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
# def categories(request, catid):
#    if request.GET:
#        print(request.GET)
#    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{cat}</p>')


# def pageNotFound(request, exeption):
#    return HttpResponse
