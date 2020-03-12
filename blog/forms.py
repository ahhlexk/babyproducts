from django import forms
from .models import Post
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

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

    class Meta:
        model = Contact
        fields = ('email', 'name','subject','message',)



