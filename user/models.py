from django.db import models
from home.models import Book
from django.contrib.auth.models import User

# Create your models here.
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Wishlist: {self.book.bookName} by {self.book.bookAuthor}, Published in {self.book.publication_date}, Genre: {self.book.genre}, Rating: {self.book.rating}, cover_image: {self.book.cover_image}, download_link: {self.book.download_link}, pk: {self.book.pk}"

class favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Wishlist: {self.book.bookName} by {self.book.bookAuthor}, Published in {self.book.publication_date}, Genre: {self.book.genre}, Rating: {self.book.rating}, cover_image: {self.book.cover_image}, download_link: {self.book.download_link}, pk: {self.book.pk}"

class read(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Wishlist: {self.book.bookName} by {self.book.bookAuthor}, Published in {self.book.publication_date}, Genre: {self.book.genre}, Rating: {self.book.rating}, cover_image: {self.book.cover_image}, download_link: {self.book.download_link}, pk: {self.book.pk}"

# Comments database
class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveIntegerField(default=5)  # Assuming a rating system
    created_at = models.DateTimeField(auto_now_add=True)
