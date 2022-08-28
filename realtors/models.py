from distutils.command.upload import upload
from pickle import FALSE, TRUE
from django.db import models
from datetime import datetime

class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo= models.ImageField(upload_to='photos/%Y/%m/%d/')
    description =  models.TextField(blank = TRUE)
    phone = models.CharField(max_length=20)
    email =  models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=FALSE)
    hire_date = models.DateTimeField(default=datetime.now, blank = TRUE)
    def __str__(self):
        return(self.name)

