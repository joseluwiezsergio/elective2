from django import forms
from .models import Products
from .models import orderc
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    class Meta :
        model = Products
        fields = "__all__"

class EditProductForm(forms.ModelForm):
    class Meta :
        model = Products
        fields = "__all__"

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1', 'password2']

        
