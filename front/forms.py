from django import forms
from front.models import County, Business, Category

class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  # globally override the Django >=1.6 default of ':'
        super(BaseForm, self).__init__(*args, **kwargs)

class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  # globally override the Django >=1.6 default of ':'
        super(BaseModelForm, self).__init__(*args, **kwargs)

class BusinessForm(BaseModelForm):	
	name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'type':'text', 'placeholder':'Business name'}))
	image = forms.ImageField(label='Select an image')
	category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Category")
	county = forms.CharField(widget=forms.HiddenInput(), initial="Nairobi")
	street_address = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'type':'text', 'placeholder':'Street address (e.g. Moi Avenue, Nairobi)'}))
	website = forms.URLField(widget=forms.TextInput(attrs={'class' : 'form-control', 'type':'text', 'placeholder':'Web URL (Optional)'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'form-control', 'type':'text', 'placeholder':'Business email'}))
	phone_number = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'type':'text', 'placeholder':'Phone number'}))
	description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':2, 'cols': 15, 'placeholder':'Brief description'}))

	class Meta:
		model = Business
		fields = ['name', 'category', 'county', 'street_address', 'email', 'phone_number', 'description']