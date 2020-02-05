from django.db import models

# Create your models here.
class education(models.Model):
    title = models.CharField(max_length=200)
    std = models.TextField()
    result = models.CharField(max_length=20)
    img = models.FilePathField(path="/img")

class skill(models.Model):
    program = models.CharField(max_length=20)
    data = models.CharField(max_length=20)
    version = models.CharField(max_length=20)
    develop = models.CharField(max_length=200)

class project(models.Model):
    title = models.CharField(max_length=20)
    des = models.TextField()
    img = models.FilePathField(path="/img")