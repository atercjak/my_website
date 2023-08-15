from django.urls import path

from . import views

app_name = 'Home'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.send_message, name='message')
]
