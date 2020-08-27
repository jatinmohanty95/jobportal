from django.db import models
from django.conf import settings
import os
# Create your models here.
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.
class jobdesc(models.Model):
    jobname=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    experience=models.CharField(max_length=100,null=True)
    qualification=models.CharField(max_length=100)

class ApplicantData(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    mobile=models.BigIntegerField(null=True)
    qualification=models.CharField(max_length=100,null=True)
    resume=models.FileField(upload_to=os.path.join(settings.MEDIA_ROOT),null=True)
    experience=models.IntegerField(null=True)
    def __str__(self):
        return self.name

class applications(models.Model):
    applicant=models.ForeignKey(ApplicantData,on_delete=models.CASCADE)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()
    qualification=models.CharField(max_length=100)
    # resume=models.FileField(upload_to='resume',null=True)
    experience=models.IntegerField(null=True)
