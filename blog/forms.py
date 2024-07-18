from django import forms
from django.contrib.auth.models import User
from blog.models import Post
from django.contrib.auth.forms import (UserCreationForm,
                                       UserChangeForm,
                                       AuthenticationForm,
                                       UsernameField)
# from django.utils.translation import gettext,gettext_lazy as_
#create your application forms here

class UserSignupForm(UserCreationForm):
    password1=forms.CharField(label='Re-Type password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Re-Type password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'username':'User Name','first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control'}),
        }


class UserLoginForm(AuthenticationForm):
   username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'})),
   password=forms.CharField(label='(Password)',strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class UserProfileForm(UserChangeForm):
    password1 = None
    date_joined = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    last_login = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    class Meta:
        model =  User
        fields =  ['username','first_name','last_name','email','date_joined','last_login']
        labels = {'email':'Email Address','first_name':'First Name'}

class AdminProfileForm(UserChangeForm):
    password1 = None
    date_joined = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'})) 
    last_joined = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'})) 
    class Meta:
        model =User
        # fields =  '__all__'
        labels = {'email':'Email'}
        exclude=['password']

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['id','title','desc','post_image']
        labels = {'title':'Title','desc':'Description','post_image':'Add Image'}
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control'}),
            }