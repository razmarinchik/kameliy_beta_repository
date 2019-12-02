from django import forms
from .models import Records

class RecordForm(forms.ModelForm):
    #master_name=forms.CharField( widget=forms.TextInput(attrs={'class':'disabled', 'readonly':'readonly'}))
    #visit_time=forms.CharField( widget=forms.TextInput(attrs={'class':'disabled', 'readonly':'readonly'}))
    class Meta:
        model = Records
        fields = ['email', 'user_name', 'master_name', 'visit_time']
