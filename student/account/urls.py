from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='login'),
    path('home', views.home,name='home'),
    path('departments', views.departments,name='departments'),
    path('gallery', views.gallery,name='gallery'),
    path('contact', views.contact,name='contact'),
]