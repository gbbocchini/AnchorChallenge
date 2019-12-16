from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit, SmartResize
from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, request

User = get_user_model()


class PhotoGallery(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    image = ProcessedImageField(
        upload_to="albums",
        processors=[ResizeToFit(750, 1260)],
        format="JPEG",
        options={"quality": 100},
    )
    likes = models.ManyToManyField(User, blank=True, related_name="photolikes")
    added = models.DateTimeField(auto_now_add=True, editable=False)
    is_visible = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "PhotoGallery"

    def get_absolute_url(self):
        return reverse("photodetail", kwargs={"pk": self.pk})

    def get_like_url(self):
        return reverse("like", kwargs={"pk": self.pk})

    def get_like_url_api(self):
        return reverse("likeapi", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.added)
