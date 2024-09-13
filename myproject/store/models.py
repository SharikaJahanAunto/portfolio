from django.db import models

# Create your models here.
class About(models.Model):
    discription = models.CharField(max_length=500)
    designation = models.CharField(max_length=100)
    sort_discription = models.CharField(max_length=500)
    birth = models.DateField()
    website_link = models.URLField(max_length=1000)
    phone = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
    age = models.IntegerField()
    degree = models.CharField(max_length=100)
    email = models.EmailField()