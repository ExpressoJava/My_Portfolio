from django.db import models

# Create your models here.
"""
Need three separate database tables for blog:
1. Post 
2. Category
3. Comment
"""


class Category(models.Model):
    name = models.CharField(max_length=20)


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    # assigns current date/time to this field whenver an instance of this class is created
    created_on = models.DateTimeField(auto_now_add=True)
    # auto_now = True - assigns the current date/time whenever an instance of this class is saved
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
