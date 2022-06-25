from django import forms
from .models import Product
from django.contrib.auth.models import User



class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = '__all__'
		exclude = ['created_by','pending','author']



class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = '__all__'
