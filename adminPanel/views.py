from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from home.models import Book
from user.models import Comment
from .models import FAQ
from .forms import editBookForm, EditCommentForm, EditFAQForm, AddFAQForm
from authentication.forms import editProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
def adminMain(request):
    book = Book.objects.count()
    comment = Comment.objects.count()
    faq = FAQ.objects.count()
    user = User.objects.count()
    return render(request, "main/adminMain.html", {'book': book, 'comment':comment, 'faq':faq, 'user':user})

@user_passes_test(is_admin)
def editBook(request):
    data = Book.objects.all()
    return render(request, "editBook/editBook.html", {'books':data})

@user_passes_test(is_admin)
def editFAQ(request):
    data = FAQ.objects.all()
    return render(request, "editFAQ/editFAQ.html", {'data': data})

@user_passes_test(is_admin)
def editComment(request):
    comments = Comment.objects.all()
    return render(request, "editComment/editComment.html", {'comments': comments})

@user_passes_test(is_admin)
def admin_editComment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = EditCommentForm(request.POST, instance=comment)

        if form.is_valid():
            form.save()
            return redirect('editFAQ')  # Redirect to the appropriate URL after saving
    else:
        form = EditCommentForm(instance=comment)

    return render(request, 'editComment/Editform.html', {'form': form})

@user_passes_test(is_admin)
def editUsers(request):
    all_users = User.objects.all()
    return render(request, "editUsers/editUsers.html", {'all_users':all_users})

@user_passes_test(is_admin)
def admin_edit_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = editProfileForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect('Home') 
    else:
        form = editProfileForm(instance=user)

    return render(request, 'account/edit.html', {'form': form})

@user_passes_test(is_admin)
def admin_editfaq(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)

    if request.method == 'POST':
        form = EditFAQForm(request.POST, instance=faq)

        if form.is_valid():
            form.save()
            return redirect('editFAQ')  # Redirect to the appropriate URL after saving
    else:
        form = EditFAQForm(instance=faq)

    return render(request, 'editFAQ/Editform.html', {'form': form})

@user_passes_test(is_admin)
def admin_addfaq(request):
    if request.method == 'POST':
        form = AddFAQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminMain')  # Redirect to the appropriate URL after saving
    else:
        form = AddFAQForm()

    return render(request, 'editFAQ/Addform.html', {'form': form})

@user_passes_test(is_admin)
def edit_BookForm(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = editBookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('editBook')  # Redirect to the appropriate URL after saving
    else:
        form = editBookForm(instance=book)
    return render(request, "editBook/editForm.html", {'form': form})
