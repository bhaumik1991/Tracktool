from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name="Register"),
    path('login/', views.handlelogin, name="HandleLogin"),
    path('logout/', views.handlelogout, name="HandleLogout")
]