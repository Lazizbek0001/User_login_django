from . import views
from django.urls import path

urlpatterns = [
    path('',views.home, name='home'),
    path('login', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
]
