from django.db import models
from django.contrib.auth.models import User, PermissionsMixin


class GalleryUser(User, PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.first_name)
