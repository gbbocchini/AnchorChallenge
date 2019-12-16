from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class GalleryUserCreation(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["username"].label = "How do you wanna be called?"
            self.fields["email"].label = "Your Email"
            self.fields["email"].required = True
