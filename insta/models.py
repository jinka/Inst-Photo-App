from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Image(models.Model):
    image=models.ImageField(upload_to = '')
    name=models.CharField(max_length=100)
    caption=models.CharField(max_length=100)
    date_created=models.DateTimeField(default=timezone.now)
    likes=models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
       ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('insta-detail',kwargs={'pk': self.pk})

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_caption(cls, id, description):
        cls.objects.filter(id=id).update(caption = caption)
    
  
