from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.CharField(max_length=500)
    

    def __str__(self):
        return self.name

class Packages(models.Model):
    slug = models.SlugField()
    image = models.ImageField()
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    package_details_subtitle = models.CharField(max_length=255)
    package_details = models.CharField(max_length=500) 
    days = models.IntegerField()
    price = models.IntegerField()



    def __str__(self):
        return self.title
    
