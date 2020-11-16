from django import forms


class NameForm(forms.Form):
    name = forms.CharField(label="Enter Name")


class AgeForm(forms.Form):
    age = forms.IntegerField(label="Enter Age")


class GFForm(forms.Form):
    gfname = forms.CharField(label="Enter GF Name")
