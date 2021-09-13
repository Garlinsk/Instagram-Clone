from django.test import TestCase
from .models import Profile, Image,Location
from django.contrib.auth.models import User
from django.db import models

# Create your tests here.


class ImageTestCase(TestCase):
    def setUp(self):
        self.new_location = Location(location='Nairobi')
        self.new_location.save()

# Creating a new Image and saving it
        self.image = Image(image_name='Beagle', description='Lovely dog',
                           image_file='images/beagle.jpg', location=self.new_location)
        self.image.save_image()

    def test_save_images(self):
        self.image.save_image()
        all_images = Image.objects.all()
        self.assertTrue(len(all_images) > 0)

class LocationTestCase(TestCase):

    def setUp(self):
        self.location = Location(location='Lagos')

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_locations(self):
        self.location.save_location()
        all_locations = Location.objects.all()
        self.assertTrue(len(all_locations) > 0)

    def test_get_locations(self):
        self.location.save_location()
        all_locations = Location.objects.all()
        self.assertTrue(len(all_locations) > 0)
