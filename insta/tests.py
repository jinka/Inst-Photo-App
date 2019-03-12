from django.test import TestCase
from .models import Image

class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.daudi= Image(image = 'image1', name='daudi',caption ='Caption 1', date_created ='2019 March, 11')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.daudi,Image))

    # Testing Save Method
    def test_save_method(self):
        self.james.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image) > 0)
