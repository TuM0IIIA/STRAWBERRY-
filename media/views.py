from django.contrib import admin
from django.urls import path, include
from media import views, images


urlpatterns = [
   path('', views.index, name="index"),
   path('images/',views.images, name='images'),
   path('media/images/',views.images, name='images'),


]


