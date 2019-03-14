from django.test import TestCase
from django.contrib.auth.models import User
from django.db import models
from .models import Image

class ImageTestCase(TestCase):

    # Set up method
    def setUp(self):
        self.user1 = User.objects.create(username='user1')
        self.image=Image.objects.create(name="Image 1",caption="Caption 1", user=self.user1)        

    def tearDown(self):
        self.image.delete()
        self.user1.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    # # Testing Save Method
    def test_save_method(self):
        self.image.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image) > 0)
