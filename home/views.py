from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm, SearchForm
from .models import Book, CartItem
from user.models import Comment, Wishlist, favourite, read
from adminPanel.models import FAQ
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Create your views here.

def index(request):
    data = Book.objects.all()
    unique_genres = list(set(book.genre for book in data))
    read_data = read.objects.all()
    return render(request, "main/home.html", {'data': data, 'unique_genres': unique_genres, 'read_data':read_data})


def book(request, pk):
    book_instance = get_object_or_404(Book, pk=pk)
    data = Wishlist.objects.all()
    favourite_data = favourite.objects.all()
    read_data = read.objects.all()
    return render(request, "book/book.html", {'book': book_instance, 'Wishlist_data': data, 'favourite_data':favourite_data, 'read_data':read_data})

def faq(request):
    data = FAQ.objects.all()
    return render(request, "FAQ/faq.html", {'data':data})

def cart(request):
    data = CartItem.objects.all()
    return render(request, "cart/cart.html", {'data':data})

# finish this
def search(request):
    if 'name_query' in request.GET:
        name_query = request.GET['name_query']
        results = Book.objects.filter(bookName__icontains=name_query)
    else:
        results = Book.objects.all()

    form = SearchForm(initial={'name_query': name_query} if 'name_query' in request.GET else {})
    return render(request, "search/search.html", {'form': form, 'results': results,})


def addBook(request):
    if request.method == 'POST':
        # Assuming you have a form for the Book model
        form = BookForm(request.POST)

        if form.is_valid():
            # Save the book to the database
            try:
                form.save()
                return redirect('Home')
            except Exception as e:
                print(e)

            # Redirect to a Home page or any other page
            return redirect('Home') 

    else:
        # If it's a GET request, render the form
        form = BookForm()
        print(form.errors)

    return render(request, "addBook/addBook.html", {'form': form})



@login_required
def submit_comment(request, book_id):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponseForbidden("Forbidden: Only logged-in users can submit comments.")
        
        comment_text = request.POST.get('comment_text')

        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return HttpResponseForbidden("Invalid book.")

        if comment_text:
            # Create a comment and assign the current user and book
            Comment.objects.create(text=comment_text, user=request.user, book=book)
            return redirect('Book', pk=book_id)
        else:
            return HttpResponseForbidden("Invalid comment submission.")
    else:
        # Handle non-POST requests if needed
        return HttpResponseForbidden("Invalid request method.")


@login_required
def delete_book(request, pk):
    if request.method == 'POST':
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return HttpResponseForbidden("Invalid book.")

        # Check if the user has the necessary permissions to delete the book
        if request.user == book.user:  # Assuming each book has a 'user' field representing the creator
            book.delete()
            return redirect('Home')
        else:
            return HttpResponseForbidden("You do not have permission to delete this book.")
    else:
        return HttpResponseForbidden("Invalid request method.")
    
def add_to_cart(request, book_id):
    book = Book.objects.get(id=book_id)
    cart_item, created = CartItem.objects.get_or_create(book=book)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('Home')

def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.quantity -= 1
    if cart_item.quantity == 0:
        cart_item.delete()
    else:
        cart_item.save()
    return redirect('Home')
