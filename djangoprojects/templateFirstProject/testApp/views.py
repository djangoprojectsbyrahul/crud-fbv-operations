from django.shortcuts import render
import datetime

# Create your views here.
def tempview(request):
    date=datetime.datetime.now()
    my_dir={'current_datetime':date}
    return render(request,'testApp/wish.html',context=my_dir)
