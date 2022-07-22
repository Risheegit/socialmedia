from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile (models.Model):
    user = models.OneToOneField (User, on_delete= models.CASCADE)
    profile_pic = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
    mobile = models.CharField(max_length = 50, default = '9123456789', blank= True, null= True)
    location = models.CharField (max_length = 100, blank = True, null = True)
    followers = models.ManyToManyField(User, blank=True, related_name='followers')
    no_of_followers = models.IntegerField(default = 0, blank = True, null = True)
    bio = models.TextField(blank = True, null = True)


    def __str__(self) :
        return f'{self.user.username} Profile'

#Watch video for profile
    
