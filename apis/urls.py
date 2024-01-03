from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'apis'

urlpatterns = [
    path('login/', LoginView, name='login_view'),
    path('register/', register_user, name='rgister'),
    path('posts/', BlogList.as_view(), name='post_list'),
    path('posts/create/', BlogCreate, name='post_create'),
    path('posts/<str:id>/', FilterBlog.as_view(), name='filter_blog'),
]
