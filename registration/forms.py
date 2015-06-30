from django import forms
from django.contrib.auth.models import User

class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  # globally override the Django >=1.6 default of ':'
        super(BaseForm, self).__init__(*args, **kwargs)

class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  # globally override the Django >=1.6 default of ':'
        super(BaseModelForm, self).__init__(*args, **kwargs)

class LoginForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'text', 'name':'username', 'placeholder':'Username'}))
	password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'password', 'name':'password', 'placeholder':'Password'}))

	class Meta:
		model = User
		fields = ['username', 'password']