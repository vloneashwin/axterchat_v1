from django.urls import path
from . import views
#setting up url patterns
#this file represents the url file of the application from the project

app_name = 'axter_chat'

urlpatterns = [
    path("", views.index, name="index"),
    path('axter/getResponse/', views.getResponse, name='getResponse'),
    path('axter/', views.axter, name='axter'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register')
]

