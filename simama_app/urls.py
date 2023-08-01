from django.urls import path
from . import views
from .views import home, user_login, register, dashboard, edit_profile,user_logout

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('edit_profile/', edit_profile, name='edit_profile'),  
    path('logout/', user_logout, name='logout'),
    path('already_logged_in/', views.already_logged_in, name='already_logged_in'),




]