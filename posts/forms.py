from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    image = forms.ImageField()
    description = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder": "Location..."}))

    class Meta:
        model = Post
        fields = ('image', 'description')
        labels = {
            'source': '',
            'description': '',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment",)
