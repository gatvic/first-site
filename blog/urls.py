from django.urls import path

from .views import *

urlpatterns = [
    path('<int:cat_id>/', by_cat, name='by_cat'),
    path('', post_list, name='post_list'),
    path('add/', PostCreateView.as_view(), name='add'),
#    path('post/<int:pk>', post_detail, name='post_detail'),
]

urlpatterns += [

]
