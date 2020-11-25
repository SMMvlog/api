from django.db import models

# Create your models here.

class Skill(models.Model):
    skill_name = models.CharField(max_length=30)
    exp_in_month = models.CharField(max_length=20)

class Experience(models.Model):
    company_name = models.CharField(max_length=30)
    roll = models.CharField(max_length=50)
    Total_worked_month = models.CharField(max_length=20)

class Education(models.Model):
    University_or_BoardName = models.CharField(max_length=100)
    Stream_Name = models.CharField(max_length=50)
    Passing_year = models.DateField()