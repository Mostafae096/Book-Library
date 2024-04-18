from django.urls import path
from . import views

urlpatterns= [
    path('adminMain/', views.adminMain, name='adminMain'),
    path('editBook/', views.editBook, name='editBook'),
    path('editBookForm/<int:pk>/', views.edit_BookForm, name='editBookForm'),
    path('editComment/', views.editComment, name='editComment'),
    path('editCommentform/<int:pk>/', views.admin_editComment, name='editCommentform'),
    path('editUsers/', views.editUsers, name='editUsers'),
    path('editUsersform/<int:pk>/', views.admin_edit_profile, name='editUsersform'),
    path('editfaqform/<int:pk>/', views.admin_editfaq, name='editfaqform'),
    path('addfaqform/', views.admin_addfaq, name='addfaqform'),
    path('editFAQ/', views.editFAQ, name='editFAQ'),

]