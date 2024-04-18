from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns= [
    path('', views.index, name='Home'),
    path('add/', views.addBook, name='addBook'),
    path('faq/', views.faq, name='faq'),
    path('search/', views.search, name='search'),
    path('book/<int:pk>/', views.book, name='Book'),
    path('submit_comment/<int:book_id>/', views.submit_comment, name='submit_comment'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('removew_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart, name='cart'),
    ]



