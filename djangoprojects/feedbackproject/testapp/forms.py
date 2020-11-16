from django import forms
from django.core import validators
#Our own validations
def only_alphabets(value):
    if value.isalpha() != True:
        raise forms.ValidationError('Only aplhabets are allowed')

#Our own validations
def starts_with_r(value):
    if value[0].lower()!='r':
        raise forms.ValidationError('Name should starts with R or r only')

#Our own validation for gamil.com
def gmail_validation(value):
    if value[len(value)-9:] != 'gmail.com':
        raise forms.ValidationError('Email should be gamil.com')

class StudentFeedbackForm(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField(validators = [gmail_validation])
    password = forms.CharField(widget = forms.PasswordInput)
    retype_password = forms.CharField(widget = forms.PasswordInput)
    feedback = forms.CharField(widget = forms.Textarea, validators = [validators.MinLengthValidator(10), validators.MaxLengthValidator(30)])

    #Single clean method for total form fields
    def clean(self):
        print('Total Form Validation....')
        cleaned_data = super().clean()
        input_name = cleaned_data['name']
        if len(input_name)<10:
            raise forms.ValidationError('Name field should have at least 10 characters')
            return input_name

        input_rollno = cleaned_data['rollno']
        if len(str(input_rollno)) !=3:
            raise forms.ValidationError('Roll number should be 3 digits only')

        input_password = cleaned_data['password']
        input_retype_password = cleaned_data['retype_password']
        if input_password != input_retype_password:
            raise forms.ValidationError("Password does not mathced, please retype same password")

    #following are explicit validations
    def clean_name(self):
        input_name = self.cleaned_data['name']
        print('Validating name')
        if len(input_name)<4:
            raise forms.ValidationError('Name field length should be equal to or greater than 4')
        return input_name

    def clean_rollno(self):
        input_rollno = self.cleaned_data['rollno']
        print('Validating rollno')
        return input_rollno

    def clean_email(self):
        input_email = self.cleaned_data['email']
        print('Validating Email')
        return input_email

    def clean_feedback(self):
        input_feedback = self.cleaned_data['feedback']
        print('Validating Feedback')
        return input_feedback
