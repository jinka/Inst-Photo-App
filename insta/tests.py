from django.test import TestCase
from . models import Image

# Create your tests here.
class CategoryTestClass(TestCase):
    def setUp(self):
        self.daudi = Image(name = 'daudd')

# Testing  instance
def test_instance(self):
    self.assertTrue(isinstance(self.daudi,Image))


# Testing Save Method
def test_save_method(self):
    self.daudi.save_editor()
    names = Image.objects.all()
    self.assertTrue(len(names) > 0)