from rest_framework import serializers
from blogplatfrm.models import User, blogs
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from datetime import datetime
from django.contrib.auth import authenticate, login


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id", "first_name", "last_name", "username"]

class LoginSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        user_name = serializers.CharField(write_only=True)
        password = serializers.CharField(write_only=True)
        if attrs['password'] and attrs['password']:
            user = authenticate(self.context.get('request'), username=user_name, password=password)
            if not user:
                raise serializers.ValidationError({"The data does not match"})
        attrs['user'] = user
        return attrs    
    

class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField( required=True,validators=[UniqueValidator(queryset=User.objects.all())])
  password = serializers.CharField(required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  
  class Meta:
    model = User
    fields = ('username', 'password', 'password2','email', 'first_name', 'last_name')
    extra_kwargs = {'first_name': {'required': True},'last_name': {'required': True}}
    
  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError({"password": "Password fields didn't match."})
    return attrs

  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name']
    )
    user.set_password(validated_data['password'])
    user.save()
    return user


class BlogSerializer(serializers.ModelSerializer):
  class Meta:
    model = blogs
    fields = ["id", "title", "content"]
    

class BlogCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = blogs
        fields = ["id", "title", "content"]

    def create(self, validated_data):
        blog = blogs.objects.create(title=validated_data['title'], content=validated_data['content'], publication_date=datetime.now())
        return blog
        