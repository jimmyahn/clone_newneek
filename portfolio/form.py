from django import forms
from .models import About
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

class AboutForm(forms.ModelForm):

    class Meta:
        model = About
        fields = ('title', 'text')