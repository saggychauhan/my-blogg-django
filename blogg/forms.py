from django import forms
from django .forms import ModelForm
from .models import Comment
from .models import Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

class postform(forms.ModelForm):
    class Meta:
        model=Post
        fields= "__all__"


