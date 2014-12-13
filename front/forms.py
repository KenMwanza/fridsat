from django import forms
from front.models import Device

class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  # globally override the Django >=1.6 default of ':'
        super(BaseModelForm, self).__init__(*args, **kwargs)

class PostDeviceForm(BaseModelForm):
    name = forms.ModelChoiceField(queryset=Device.objects.all(), empty_label="Name")
    class Meta:
        model = Device
        fields = ['name']
