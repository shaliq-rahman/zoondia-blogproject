from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'blogplatfrm'

urlpatterns = [
    path('', welcome, name='welcome'),
    path('login/', UserLogin.as_view(), name='login'),
    path('signup/', UserRegister.as_view(), name='signup'),
    path('create/', UserBlogs.as_view(), name='blogs_create'),
    path('view/', ViewBlogs.as_view(), name='blogs_view'),
]
