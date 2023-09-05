from django import forms
from .models import product,chat_comment,chat_post,choice,post,chat_post
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

class post_adding_form(forms.ModelForm):
    class Meta:
        model = post
        fields = '__all__'          

class choice_adding_form(forms.ModelForm):
    class Meta:
        model = choice
        fields = '__all__'    

class chat_post_adding_form(forms.ModelForm):
    class Meta:
        model = chat_post
        fields = '__all__'        