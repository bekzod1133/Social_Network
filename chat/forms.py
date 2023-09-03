from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    model = Message
    fields = ['body']
