from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('', views.index, name="HomePage"),
    path("contact/", views.contact, name="ContactUs"),
    path("about/", views.about, name="AboutUs"),
    path("service/", views.service, name="Services"),
    path("post/", views.post, name="PostAD"),
]
