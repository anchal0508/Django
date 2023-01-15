from django.urls import path
from app1 import views

app_name = 'app1'
urlpatterns = [
    path('', views.index, name= 'home'),
    path('contact/', views.contact, name= 'contact'),
]