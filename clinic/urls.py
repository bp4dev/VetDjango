from django.urls import path
from . import views

urlpatterns = [
    path ('',views.main, name="main"),
    path ('contact.html',views.contact, name="contact"),
    path ('gallery.html',views.gallery, name="gallery"),
    path ('about.html',views.about, name="about"),
    ]