from django.db import models

# Create your models here.
class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    new_phno=models.CharField(max_length=10)

   
    

   
