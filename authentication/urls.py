from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns= [
    path('logout/', auth_views.LogoutView.as_view(next_page='Home'), name='logout'),
    path('login/', views.userlogin, name='login'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit_profile, name='Edit'),
]