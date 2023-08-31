from django.db import models

# Create your models here.

class BlogPost(models.Model):
  title = models.CharField(max_length=255)
  content = models.CharField(max_length=255)
  pub_date = models.DateField()
  author = models.CharField(null=True, max_length=255)

class Product(models.Model):
  name = models.CharField(max_length=255)
  price = models.IntegerField(max_length=10)
  description = models.CharField(max_length=999)
