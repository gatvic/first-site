from django.urls import path

from .views import *

urlpatterns = [
    path('', post_list),
#    path('post/<int:pk>', post_detail, name='post_detail'),
]

urlpatterns += [
    path('/int:cat_id>/', by_cat, name='by_cat'),
]
