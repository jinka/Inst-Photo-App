from django.test import TestCase
from .models import Image

class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.daudi= Image(image = 'image1', name='daudi',caption ='Caption 1',likes='1',user_id=1)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.daudi,Image))

    # Testing Save Method
    def test_save_method(self):
        self.daudi.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image) > 0)
