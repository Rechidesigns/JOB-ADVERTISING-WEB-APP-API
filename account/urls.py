from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from . import views

admin.site.register(User, UserAdmin)

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('access_token/', include('djoser.urls.jwt')),
    path("login", views.login_view), 
    path("logout", views.logout_view)
]



