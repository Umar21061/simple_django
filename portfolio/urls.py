from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # This is your default homepage URL
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('homepage/', views.homepage, name='homepage_alternate'),  # New URL pattern for /homepage/
]
