from django import forms
from .models import MessageModel
from django.forms import ValidationError


class MessageForm(forms.ModelForm):
    class Meta:
        model = MessageModel
        fields = ['name', 'email', 'subject', 'message']

        
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) > 100:
            raise ValidationError("name can't have more than 100 letter")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if len(email) > 254:
            raise ValidationError("email can't have more than 254 letter")
        return email

    def clean_subject(self):
        subject = self.cleaned_data.get('subject')
        if len(subject) > 150:
            raise ValidationError("subject can't have more than 150 letter")
        return subject

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) > 3000:
            raise ValidationError("message can't have more than 3000 letter")
        return message
    