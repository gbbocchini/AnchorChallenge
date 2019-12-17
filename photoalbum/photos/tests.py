from django.test import Client, TestCase, override_settings
from django.urls import reverse, reverse_lazy
from django.conf import settings
from model_mommy import mommy
from .models import PhotoGallery


class PhotoGalleryModelTest(TestCase):
    print("** Setting up for PhotoGallery model and views tests \n -this can take a minute due free hosted MongoDb :]", flush=True)

    def setUp(self):
        self.photogallery = mommy.make(PhotoGallery)

    def test_get_absolute_url(self):
        self.assertEquals(
            self.photogallery.get_absolute_url(),
            reverse('photodetail', kwargs={'pk': self.photogallery.pk})
        )
        print("***get_absolute_url test ended***", flush=True)

    def test_get_like_url(self):
        self.assertEquals(
            self.photogallery.get_like_url(),
            reverse('like', kwargs={'pk': self.photogallery.pk})
        )
        print("***get_like_url test ended***", flush=True)

    def test_get_like_url_api(self):
        self.assertEquals(
            self.photogallery.get_like_url_api(),
            reverse('likeapi', kwargs={'pk': self.photogallery.pk})
        )
        print("***get_like_url_api test ended***", flush=True)


class PhotoGalleryViewsTest(TestCase):
    def setUp(self):
        self.url = reverse('allphotos')
        self.client = Client()
        self.photogallery = mommy.make(PhotoGallery, _quantity=10)

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        print("***list_view test ended***", flush=True)
