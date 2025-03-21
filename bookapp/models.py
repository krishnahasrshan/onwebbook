from django.db import models
from django.contrib.auth.models import user 
class  UserProfile(models.Model):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length="20")

    def __str__(self):
        return self.email 
    
class user():
    print()