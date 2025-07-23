from django import forms
from .models import Blog
from django.core.exceptions import ValidationError


class BlogForm(forms.Form):
    class Meta:
        model = Blog
        exclude = ("count_of_views",)