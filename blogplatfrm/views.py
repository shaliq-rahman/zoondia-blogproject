from django.shortcuts import render
from django.views import View
from .forms.account import SignupForm, SignInForm
from .forms.blogs import BlogEntryForm
from .models import User, blogs
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
import pdb


# Create your views here.


def welcome(request):
    return render(request, 'welcome.html')


class UserLogin(View):
    def get(self, request, *args, **kwargs):
        form = SignInForm()
        return render(request, 'login.html', context={'form':form})
    
    
    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)
        if form.is_valid():
            email =  request.POST.get('email', None)
            password = request.POST.get('password', None)
            user = authenticate(email=email, password=password)
            login(request, user)
        return HttpResponseRedirect('/')

    
class UserRegister(View):
    def get(self, request, *args, **kwargs):
        form = SignupForm()
        return render(request, 'signup.html', context={'form':form})

    def post(self, request, *args, **kwargs):
        form = SignupForm(request.POST)
        if form.is_valid():
            first_name = request.POST.get('first_name', None)
            last_name = request.POST.get('last_name', None)
            user_name = request.POST.get('user_name', None)
            password = request.POST.get('password', None)
            email = request.POST.get('email', None)
            
            new_password = make_password(password)
            User.objects.create(first_name=first_name, last_name=last_name, email=email, password=new_password, user_name=user_name)
            return HttpResponseRedirect('/blogs/login/')
        else:
            print(form.errors)
            form = SignupForm()
            return render(request, 'signup.html', context={'form':form})
        
        


class ViewBlogs( View):    
    def get(self, request, *args, **kwargs):
        blogs_ = blogs.objects.filter(is_active=True)
        return render(request, 'blogs.html', context={'blogs':blogs_})

    
    
class UserBlogs(View):
    def get(self, request, *args, **kwargs):
        form = BlogEntryForm()
        return render(request, 'blogform.html', context={'form':form})
    
    
    def post(self, request, *args, **kwargs):
            title = request.POST.get('title', None)
            content =  request.POST.get('content', None)
            blogs.objects.create(user_id=request.user.id, title=title, content=content, publication_date=datetime.now(), updated_at=datetime.now())
            return HttpResponseRedirect('/blogs/view/')

