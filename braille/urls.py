from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('speak/', views.on_speak_now, name='on_speak'),
    path('contact-us/', views.contact, name='contact')
]