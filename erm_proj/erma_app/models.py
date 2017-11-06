from django.db import models
from django.contrib.auth.models import User

# builtin User model application

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)
    external_site = models.URLField(blank=True)
    profile_image = models.ImageField(upload_to='profile_image',blank=True)

    def __str__(self):
        return self.user.username







# Create your models here.

class Topic(models.Model):
    topic_name = models.CharField(max_length=256,unique=True)  # w/ Primary Key

    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=256,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage)
    date = models.DateField()

    def __str__(self):
        return self.date
