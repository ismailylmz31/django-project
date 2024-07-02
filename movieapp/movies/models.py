from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    film_adi=models.CharField(max_length=100)
    film_aciklamasİ=models.TextField()
    resim=models.CharField(max_length=100)
    anasayfa=models.BooleanField(default=False)