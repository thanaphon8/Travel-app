from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('', views.homePage, name='home'),
    path('nav/', views.navebar, name='nav'),
    path('contact/', views.contactPage, name='contact'),
    path('travel/', views.travelPage, name='travel'),
]
