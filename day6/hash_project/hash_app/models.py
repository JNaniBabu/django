from django.db import models

# Create your models here.

class users(models.Model):
      user_name=models.CharField(max_length=30)
      password=models.CharField(max_length=100)
      mobile=models.CharField(max_length=30)
      reg_date=models.DateField()
      
