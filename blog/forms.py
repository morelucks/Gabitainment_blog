from django import forms
from django.forms import ModelForm
from .models import Comment,Post
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=["post"]
        labels={
            "user_name":"Your Name",
            "user_email":"Your Email",
            "text":"Comment"
        }

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        # exclude=["title"]
        fields='__all__'