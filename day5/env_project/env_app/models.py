from django.db import models


# Create your models here.

class Sample_table(models.Model):
    name=models.CharField(max_length=30)
    mobile=models.CharField(max_length=30)
