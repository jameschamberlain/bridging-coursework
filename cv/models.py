from django.db import models

# Create your models here.
class WorkExperience(models.Model):
    role = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    details = models.TextField()

class Education(models.Model):
    institution = models.CharField(max_length=50)
    details = models.TextField()

class Project(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField()

class Skill(models.Model):
    name = models.CharField(max_length=50)