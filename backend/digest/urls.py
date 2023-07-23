from django.urls import path

from . import views

urlpatterns = [
    path('createdigest/', views.create_digest, name='Create digest'),
]