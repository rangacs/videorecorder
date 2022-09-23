from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import VideoLib  
from django import forms


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreateForm(forms.Form):  
    name = forms.CharField(label="Enter  name",max_length=50)  
    mobile  = forms.CharField(label="Enter mobile", max_length = 10)  
    file = forms.FileField(label="Chose Video File")
   

class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = VideoLib  
        fields = "__all__"            


