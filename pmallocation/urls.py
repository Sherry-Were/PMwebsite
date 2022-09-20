from zoneinfo import reset_tzpath
from django.contrib import admin
from django.urls import path, include, re_path

from django.contrib.auth import views as auth_views
from users import views as user_views
from . import views

urlpatterns = [
    path('home', views.welcome, name='home page'),
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='log_in page'),
    path('signup/', user_views.signup, name='signup'),
    path('dkghggn', views.photos, name='photos'),
    path('regiuduifr', views.register, name='register'),
    path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='log out'),
    
]