from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Register(UserCreationForm):
    email=forms.EmailField()
    fname=forms.CharField(max_length=30)
    lname=forms.CharField(max_length=30)

    regno=forms.CharField(max_length=30)
    course=forms.CharField(max_length=30)
    year=forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = ['fname','lname','regno' ,'course','email','password1','password2']
        def save(self,commit=True):
            user=super(Register,self).save(commit=True)
            user.regno=self.cleaned_data['regno']
            user.course=self.cleaned_data['regno']
            user.year=self.cleaned_data['regno']
            if commit:
                user.save()
            return user
