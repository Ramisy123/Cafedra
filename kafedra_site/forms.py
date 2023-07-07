from dataclasses import fields
from socket import fromshare
from xml.dom import ValidationErr
from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, Group

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = {'photo'}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-control'

class RateForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('name','text', 'file')
        widgets = {
          'name': forms.Textarea(attrs={'rows':1, 'cols':10, 'color': '#fff'}),
          'text': forms.Textarea(attrs={'rows':2, 'cols':10, 'color': '#fff'}),
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'