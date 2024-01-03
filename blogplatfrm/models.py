from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=250, null=False, blank=False)
    last_name = models.CharField(max_length=250, null=False, blank=False)
    user_name = models.CharField(max_length=25, null=False, blank=False, unique=True)
    email = models.CharField(max_length=25, null=False, blank=False)
    password = models.CharField(max_length=250, null=False, blank=False)
    
    def __str__(self):
      return "{}".format(self.email)
    

class blogs(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, related_name="user_blogs", on_delete=models.CASCADE)
    title =  models.CharField(max_length=250, null=False, blank=False)
    content =  models.TextField()
    publication_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
      return "{}".format(self.title)
    
