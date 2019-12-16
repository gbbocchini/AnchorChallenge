from django.shortcuts import get_object_or_404
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    RedirectView,
)
from .models import PhotoGallery
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


class Home(TemplateView):
    template_name = "index.html"


# send pic
class PicSend(LoginRequiredMixin, CreateView):
    model = PhotoGallery
    fields = [
        "image",
    ]
    success_url = "allphotos"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# pic detail
class PicDetail(LoginRequiredMixin, DetailView):
    model = PhotoGallery


# listPics
class PicList(LoginRequiredMixin, ListView):
    model = PhotoGallery
    queryset = PhotoGallery.objects.filter(is_visible=True)
    paginate_by = 12


class PicListByAdded(LoginRequiredMixin, ListView):
    model = PhotoGallery
    queryset = PhotoGallery.objects.filter(is_visible=True).order_by("-added")
    paginate_by = 12


class LikeToggle(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        pk_ = self.kwargs.get("pk")
        obj = get_object_or_404(PhotoGallery, pk=pk_)
        url_ = obj.get_absolute_url()
        user_ = self.request.user
        if user_.is_authenticated:
            if user_ in obj.likes.all():
                obj.likes.remove(user_)
            else:
                obj.likes.add(user_)
        return url_


class LikeToggleAPI(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk=None, format=None):
        obj = get_object_or_404(PhotoGallery, pk=pk)
        user = self.request.user
        updated = False
        liked = False
        if user.is_authenticated:
            if user in obj.likes.all():
                liked = False
                obj.likes.remove(user)
            else:
                liked = True
                obj.likes.add(user)
                updated = True
        data = {"updated": updated, "liked": liked}
        return Response(data)
