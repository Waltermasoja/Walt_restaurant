from django import forms
from .models import product,chat_comment,chat_post,choice
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class make_order(forms.ModelForm):
    class Meta:
        model = product
        fields = '__all__'

class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",'email',"password1","password2",)

class comments_form(forms.ModelForm):
    class Meta:
        model = chat_comment
        fields = ['author','comment_text',]     