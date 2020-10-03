from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userInformation(models.Model):
    imageName= models.CharField(max_length= 100, blank=False)
    Image = models.FileField( upload_to= 'images/dataImage', blank=True)
    Date = models.CharField(max_length=100, blank=False)
    Time = models.CharField(max_length= 100, blank= True)

    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)

