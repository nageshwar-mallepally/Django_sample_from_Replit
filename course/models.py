from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    lecturer = models.CharField(max_length=15)
    fee = models.FloatField(max_length=6)
