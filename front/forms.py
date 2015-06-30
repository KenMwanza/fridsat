from django import forms
from front.models import Device

class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  # globally override the Django >=1.6 default of ':'
        super(BaseForm, self).__init__(*args, **kwargs)

class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  # globally override the Django >=1.6 default of ':'
        super(BaseModelForm, self).__init__(*args, **kwargs)

class PostDeviceForm(BaseModelForm):
    name = forms.ModelChoiceField(queryset=Device.objects.all(), empty_label="Name")

    class Meta:
        model = Device
        fields = ['name']

class PublishForm(BaseForm):
	CATEGORIES = (
	('Tablet', 'Tablet'),
	('Smartphone', 'Smartphone'),
	('Accessory', 'Accessory'),
	)
	
	title = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'type':'text', 'placeholder':'Title (e.g. Apple iPad2 Air 64 GB)'}))
	name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'type':'text', 'placeholder':'Name (e.g. Samsung Galaxy Trend)'}))
	brand = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'type':'text', 'placeholder':'Brand (e.g. Nokia, Samsung, etc)'}))
	question_text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':2, 'cols': 15}), label="Question")
	price = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'type':'text'}))
	categories = forms.CharField(widget=forms.Select(choices=CATEGORIES))