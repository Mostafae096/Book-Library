from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse
from authentication.models import UserProfile
from .models import Wishlist, favourite, read
from home.models import Book

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        # Retrieve user data
        user_data = User.objects.get(pk=request.user.id)

        # Retrieve user profile data
        user_profile_data = UserProfile.objects.get(user=request.user)
        data = Wishlist.objects.all()
        favourite_data = favourite.objects.all()
        read_data = read.objects.all()
        # Pass both sets of data to the template
        return render(request, "main/profile.html", {'user_data': user_data, 'user_profile_data': user_profile_data, 'Wishlist_data': data, 'favourite_data':favourite_data, 'read_data':read_data})
    else:
        # Handle the case when the user is not logged in
        return render(request, "main/profile.html", {'user_data': None, 'user_profile_data': None})
    
def add_to_wishlist(request, book_id):
    book = Book.objects.get(pk=book_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, book=book)
    if created:
        return redirect('profile')
    return redirect('profile')

def add_to_favourite(request, book_id):
    book = Book.objects.get(pk=book_id)
    favourite_item, created = favourite.objects.get_or_create(user=request.user, book=book)
    if created:
        return redirect('profile')
    return redirect('profile')

def add_to_read(request, book_id):
    book = Book.objects.get(pk=book_id)
    read_item, created = read.objects.get_or_create(user=request.user, book=book)
    if created:
        return redirect('profile')
    return redirect('profile')

def remove_from_wishlist(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    # Assuming there's a ForeignKey relationship from Wishlist to Book with a related_name 'wishlist_items'
    wishlist_item = Wishlist.objects.filter(user=request.user, book=book).first()
    
    if wishlist_item:
        wishlist_item.delete()

    return redirect('profile')

def remove_from_favourite(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    # Assuming there's a ForeignKey relationship from Wishlist to Book with a related_name 'wishlist_items'
    favourite_item = favourite.objects.filter(user=request.user, book=book).first()
    
    if favourite_item:
        favourite_item.delete()

    return redirect('profile')

def remove_from_read(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    # Assuming there's a ForeignKey relationship from Wishlist to Book with a related_name 'wishlist_items'
    read_item = read.objects.filter(user=request.user, book=book).first()
    
    if read_item:
        read_item.delete()

    return redirect('profile')