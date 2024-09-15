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

    def __str__(self):
        return self.email

class Social(models.Model):
    social_icon = models.CharField(max_length=100, default='empty')
    link = models.URLField(max_length=1000)

    def __str__(self):
        return self.social_icon

class Service(models.Model):
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    image= models.ImageField(upload_to='Service/',blank=True, null=True)
    discription= models.CharField(max_length=500)
    