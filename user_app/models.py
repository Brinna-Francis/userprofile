from django.db import models



# Create your models here.


class Profile(models.Model):
    username = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    location = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15, blank=True)
    age = models.IntegerField()
    qualifications = models.CharField(max_length=255, default='None')
    skills = models.TextField(blank=True)
    certifications = models.CharField(max_length=255, null=False, blank=False)
    work_experience = models.IntegerField()



class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    project_image = models.ImageField(upload_to='project_images/')







