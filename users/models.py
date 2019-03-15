from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from tinymce.models import HTMLField
# 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    bio=HTMLField(default="default bio")


    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self,**kwargs):
        super().save()


class UserFollowing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userfollowto")
    user_following=models.ForeignKey(User, on_delete=models.CASCADE, related_name="userfollowing")  

class UserFollower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userfollowedby")
    user_follower= models.ForeignKey(User, on_delete=models.CASCADE, related_name="userfollower")  


