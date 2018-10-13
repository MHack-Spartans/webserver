from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('learn', views.learn, name='learn'),
    path('register/', views.register, name='register'),
    path('register_success/', views.register_success, name='register_success'),
]