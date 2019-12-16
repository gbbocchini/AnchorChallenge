from django.contrib import admin
from django.urls import path, include
from photos import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "photos"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.Home.as_view(), name="home"),
    path("accounts/", include("accounts.urls"), name="accounts"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("uploadpic", views.PicSend.as_view(), name="uploadpic"),
    path("allphotos", views.PicList.as_view(), name="allphotos"),
    path(
        "allphotos/bydateadded", views.PicListByAdded.as_view(), name="allphotosbyadded"
    ),
    path("photodetail/<pk>", views.PicDetail.as_view(), name="photodetail"),
    path("photodetail/<pk>/like", views.LikeToggle.as_view(), name="like"),
    path("api/photodetail/<pk>/like", views.LikeToggleAPI.as_view(), name="likeapi"),
]
