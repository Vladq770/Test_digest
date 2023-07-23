from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("core/", include("core.urls")),
    path("digest/", include("digest.urls")),
    path("admin/", admin.site.urls),
]
