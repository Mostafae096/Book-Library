# forms.py
from django import forms
from .models import Book  # Assuming you have a Book model

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['bookName', 'bookAuthor', 'publication_date', 'genre', 'rating', 'cover_image', 'download_link']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add custom classes and IDs to form fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-input', 'id': field_name})

class SearchForm(forms.Form):
    name_query = forms.CharField(max_length=100, required=False, label='Book name', widget=forms.TextInput(attrs={'class': 'search-bar', 'id': 'search-input'}))
    # author_query = forms.CharField(max_length=100, required=False, label='Book author')
    # date_query = forms.CharField(max_length=100, required=False, label='Publication date')
    # genre_query = forms.CharField(max_length=100, required=False, label='Genre')