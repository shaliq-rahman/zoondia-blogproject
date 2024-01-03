from django.shortcuts import render
from .serializers.account import RegisterSerializer, BlogSerializer, BlogCreateSerializer, LoginSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from blogplatfrm.models import blogs
from rest_framework.views import APIView
from django.contrib.auth import login

# Create your views here.

class LoginView(APIView):
    
    def post( self, request):
        serializer = LoginSerializer(data=self.request.DATA)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(status= status.HTTP_202_ACCEPTED)
    
        
@api_view(['POST'])
def register_user(request):
    serilaized_data = RegisterSerializer(data=request.DATA)
    if serilaized_data.is_valid():
        return Response(serilaized_data, status=status.HTTP_201_CREATED)


class BlogList(generics.ListCreateAPIView):
    queryset = blogs.objects.all()
    serializer_class = BlogSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)
    

@api_view(['POST'])
def BlogCreate(request):
    serilaized_data = BlogCreateSerializer(data=request.DATA)
    if serilaized_data.is_valid():
        return Response(serilaized_data, status=status.HTTP_201_CREATED)
    

class FilterBlog(APIView):
    def get(self, request, *args, **kwargs):
        id = self.kwargs['id']
        try:
            blog = blogs.objects.get(id=id)
            serializer = BlogSerializer(blog, many=False)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)    
    
    def delete(self, request, *args, **kwargs):
        id = self.kwargs['id']
        try:
            blog = blogs.objects.get(id=id)
            blog.delete()
            return Response('Data deleted successfully', status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)  
        
        
