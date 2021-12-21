from django.db import models

# Create your models here.
class Student(models.Model):
  name = models.TextField()
  address = models.TextField()
  branch = models.TextField()