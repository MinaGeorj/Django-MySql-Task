from django import forms
from device.models import Device
class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = "__all__"
