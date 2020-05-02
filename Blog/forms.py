from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'text')

        widget = {
            'title': forms.TextInput,
            'text': forms.Textarea
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')

        widget = {
             'author': forms.TextInput,
             'text': forms.Textarea
        }
