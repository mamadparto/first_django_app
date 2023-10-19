from django import forms
from .models import Posts


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ["title", "text", "author", "status"]
