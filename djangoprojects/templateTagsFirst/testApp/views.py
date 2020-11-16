from django.shortcuts import render
import datetime

# Create your views here.
def date_info(request):
    name='Hridhan'
    date=datetime.datetime.now()
    h=int(date.strftime("%H"))
    msg=''
    if h<12:
        msg="Good Morning!!!!"
    elif h<16:
        msg="Good Afternoon!!!!"
    elif h<22:
        msg="Good Evening!!!!"
    else:
        msg="Good Night!!!!"

    my_dir={'guest':name,'date':date,'message':msg}
    return render(request,'testApp/wish.html',context=my_dir)
