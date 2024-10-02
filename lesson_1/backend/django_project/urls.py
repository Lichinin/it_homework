from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('first_app.urls')),
    path("", include('second_app.urls')),
    path("", include('third_app.urls')),
]
