from django.urls import path
from . import views

urlpatterns= [
    path('profile/', views.index, name='profile'),
    path('wishlist/add/<int:book_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('favourite/add/<int:book_id>/', views.add_to_favourite, name='add_to_favourite'),
    path('read/add/<int:book_id>/', views.add_to_read, name='add_to_read'),
    path('wishlist/remove/<int:book_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('favourite/remove/<int:book_id>/', views.remove_from_favourite, name='remove_from_favourite'),
    path('read/remove/<int:book_id>/', views.remove_from_read, name='remove_from_read'),
    
]