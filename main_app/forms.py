from django import forms
from .models import Records

class RecordForm(forms.ModelForm):
    class Meta:
        model = Records
        fields = ['email', 'user_name', 'visit_time', 'master_name']
