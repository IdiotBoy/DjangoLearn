from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    headImg  = models.FileField(upload_to='./upload/')
    
    def __unicode__(self):
        return self.username

class Employee(models.Model):
    name = models.CharField(max_length=20)
    
    def __unicode__(self): # toString()
        return self.name

class Entry(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name

class Blog(models.Model):
    name = models.CharField(max_length=30)
    entry = models.ForeignKey(Entry)
    
    def __unicode__(self):
        return self.name