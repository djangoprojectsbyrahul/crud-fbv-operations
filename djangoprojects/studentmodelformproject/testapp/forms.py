from django import forms
from . import models

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.StudentRegister
        fields = '__all__'
