# forms.py
from django import forms
from home.models import Book  
from .models import FAQ  
from user.models import Comment 

class editBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['bookName', 'bookAuthor', 'publication_date', 'genre', 'rating', 'cover_image', 'download_link']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add custom classes and IDs to form fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-input', 'id': field_name})


class EditFAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add custom classes and IDs to form fields
        self.fields['question'].widget.attrs.update({'class': 'form-input', 'id': 'question'})
        self.fields['answer'].widget.attrs.update({'class': 'form-input', 'id': 'answer'})

class AddFAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add custom classes and IDs to form fields
        self.fields['question'].widget.attrs.update({'class': 'form-input', 'id': 'question'})
        self.fields['answer'].widget.attrs.update({'class': 'form-input', 'id': 'answer'})

class EditCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'rating']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add custom classes and IDs to form fields
        self.fields['text'].widget.attrs.update({'class': 'form-input', 'id': 'text'})
        self.fields['rating'].widget.attrs.update({'class': 'form-input', 'id': 'rating'})
