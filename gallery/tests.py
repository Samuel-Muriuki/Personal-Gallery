from email.mime import image
from unicodedata import category
from django.test import TestCase

from gallery.models import Category, Image, Location

# Create your tests here.
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.image = Image(image = 'image', category = 'tech', location = 'nairobi', description = 'nice')
        self.image.save_image()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    # Testing save method
    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    # Testing delete method
    def test_delete(self):
        self.image.save()
        self.image.delete()
        self.assertTrue(len(Image.objects.all() == 0))

    # Testing the search image
    def test_search_image(self):
        self.image.save()
        image = Image.search_image('tech')
        self.assertTrue(len(image) > 0)

class LocationTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.locations = Location.objects.create(location = 'nairobi')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.locations, Location))

class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.category = Category.objects.create(category = 'tech')

     # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))
