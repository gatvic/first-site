from django.shortcuts import render
# from django.http import HttpResponse, Http404
# Create your views here.


def post_list(request):
    return render(request, 'blog/base.html', {})


# def categories(request, catid):
#    if request.GET:
#        print(request.GET)
#    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{cat}</p>')


# def pageNotFound(request, exeption):
#    return HttpResponse
