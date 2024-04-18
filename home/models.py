# models.py
from django.db import models
from django.contrib.auth.models import User

# Books database
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=6)  # Use a valid user ID
    bookName = models.CharField(max_length=200)
    bookAuthor = models.CharField(max_length=200)
    publication_date = models.CharField(max_length=4)
    genre = models.CharField(max_length=100)
    rating = models.IntegerField(default=5)
    cover_image = models.CharField(max_length=500)
    download_link = models.CharField(max_length=500)
    price = models.IntegerField()

class CartItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)