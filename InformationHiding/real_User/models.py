from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    #eta profile er model/table.. aro kichu add koris..add image
    #userName = models.CharField(max_length=100, blank= False, unique= True) ei username ta hobe kina sure na ami.. tui jkhn profile kaaj korbi tkhn to dekhbii.
    FirstName= models.CharField(max_length=100, blank= True)
    LastName = models.CharField(max_length=100, blank= True)
    Phone_No = models.IntegerField(blank=True, null= True)
    EmailID = models.EmailField(max_length=100, unique= True)
    Occupation = models.CharField(max_length=100, blank= True)
    City = models.CharField(max_length= 100, blank= True)
    Country = models.CharField(max_length=100,blank=True)
    user = models.ForeignKey(User, default= None, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

