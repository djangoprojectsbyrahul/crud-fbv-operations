from django import forms
from blog.models import Comment


class EmailSendForm(forms.Form):
    sender_name = forms.CharField()
    sender_email = forms.EmailField()
    receiver_email = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class WhatsappSendForm(forms.Form):
    receiver_mobile_number = forms.IntegerField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
