from django.contrib import admin
from photos.models import PhotoGallery
from django.utils.safestring import mark_safe


# admin.site.register(PhotoGallery)


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    readonly_fields = ["likes"]
    list_display = (
        "added",
        "user",
        "photo",
        "is_visible",
    )
    list_filter = ("added", "is_visible", "likes")

    def photo(self, obj):
        return mark_safe(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.image.url, width=200, height=200,
            )
        )
