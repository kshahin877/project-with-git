from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# creating a post author
class Author(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    def __str__(self):
        return self.name


# creating a post category
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


# create a post for blog
class Post(models.Model):
    title=models.CharField(max_length=500)
    description=models.TextField(blank=False)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title



