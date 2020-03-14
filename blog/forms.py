from django import forms
from .models import Post
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget



class PostForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    text = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Post'}))
    class Meta:
        model = Post
        fields = (
            'title', 
            'text', 
            'tags',
            )

class SubscriberForm(UserCreationForm):
    email = forms.EmailField(
        required=True, widget=forms.TextInput(attrs={'class':'form-control'})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    password1 = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'})
    )
    password2 = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'})
    )

class ContactForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    subject = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Message'}))
    class Meta:
        model = Contact
        fields = ('email', 'name','subject','message',)



