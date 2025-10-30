from django import forms
from .models import MessageModel


class MessageForm(forms.ModelForm):
    class Meta:
        model = MessageModel
        fields = ['name', 'email', 'subject', 'message']
