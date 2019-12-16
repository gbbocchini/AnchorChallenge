from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import GalleryUserCreation


class Register(CreateView):
    form_class = GalleryUserCreation
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"
