from django.shortcuts import render
from . import forms

# Create your views here.
def thankyou_view(request):
    return render(request,'testapp/thankyou.html')

def student_feedback(request):
    if request.method == 'GET':
        form = forms.StudentFeedbackForm()
        return render(request, 'testapp/feedback.html', {'form':form})
    if request.method == 'POST':
        form = forms.StudentFeedbackForm(request.POST)
        if form.is_valid():
            print('Validation completed....Printing feedback form Information....')
            print('Student name: ',form.cleaned_data['name'])
            print('Student roll number: ', form.cleaned_data['rollno'])
            print('Student email: ', form.cleaned_data['email'])
            print('Student feedback: ', form.cleaned_data['feedback'])
            return thankyou_view(request)
    return render(request, 'testapp/feedback.html', {'form':form})
