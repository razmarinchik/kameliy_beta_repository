from django import forms
from .models import Records

class RecordForm(forms.ModelForm):
    #master_name=forms.CharField(widget=forms.HiddenInput())#disabled = True)
    #visit_time=forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Records
        fields = ['email', 'user_name', 'master_name', 'visit_time']
