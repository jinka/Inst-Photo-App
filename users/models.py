from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from tinymce.models import HTMLField
from insta.models import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    bio=HTMLField(default="default bio")


    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self,**kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class UserFollowing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userfollowto")
    user_following=models.ForeignKey(User, on_delete=models.CASCADE, related_name="userfollowing")  

class UserFollower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userfollowedby")
    user_follower= models.ForeignKey(User, on_delete=models.CASCADE, related_name="userfollower")  


class Comments(models.Model):
    comment = models.TextField()
    posted_on = models.DateTimeField(auto_now=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()
