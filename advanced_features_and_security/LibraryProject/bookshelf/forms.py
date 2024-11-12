rom django import forms
from .models import Book
from django.core.exceptions import ValidationError
import bleach

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'summary', 'published_date']
        
    def clean_title(self):
        title = self.cleaned_data.get('title')
        # Strip unwanted HTML tags to prevent XSS attacks
        title = bleach.clean(title, tags=[], strip=True)
        return title

    def clean_summary(self):
        summary = self.cleaned_data.get('summary')
        # Allow basic formatting tags only
        summary = bleach.clean(summary, tags=['b', 'i', 'u', 'p', 'br', 'ul', 'li', 'ol'], strip=True)
        return summary

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        summary = cleaned_data.get("summary")

        if title and summary and len(summary) < 20:
            raise ValidationError("Summary should be at least 20 characters long.")
        
        return cleaned_data
