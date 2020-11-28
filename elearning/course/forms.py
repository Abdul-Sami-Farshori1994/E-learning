from django import forms
from .models import *


class studentform(forms.ModelForm):
	fname=forms.CharField()
	lname=forms.CharField()
	courses=forms.CharField()
	userid=forms.CharField()
	passwd=forms.CharField(widget=forms.PasswordInput)


	class Meta:
		model=student
		fields='__all__'
