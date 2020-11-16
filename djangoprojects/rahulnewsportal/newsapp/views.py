from django.shortcuts import render

# Create your views here.
def home(request):
    head_msg='Welcome To RAHUL News App'
    slogan='Continuous news updates....'
    my_dir={'head_msg':head_msg,'slogan':slogan}
    return render(request,'newsapp/index.html',context=my_dir)

def sports_info(request):
    head_msg='Latest Sports Information'
    msg_first='Sachin is now mentor of Mumbai Indians'
    msg_second='Dhoni declared his retirement from all international cricket'
    msg_third='IPL will be start in September in UAE'
    my_dir={'head_msg':head_msg,'msg_first':msg_first,'msg_second':msg_second,'msg_third':msg_third}
    return render(request,'newsapp/news.html',context=my_dir)

def movies_info(request):
    head_msg='Latest Movies Information'
    msg_first='SADAK 2(flop show) streaming on netflix....'
    msg_second='Stranger Things season 4 announced!!!!'
    msg_third='Rangasthalam a bautiful movie by Ramcharan!'
    my_dir={'head_msg':head_msg,'msg_first':msg_first,'msg_second':msg_second,'msg_third':msg_third}
    return render(request,'newsapp/news.html',context=my_dir)

def politics_info(request):
    head_msg='Latest Politics Information'
    msg_first='SSR Suicide is main issue....'
    msg_second='Chor ke sath mor(peacock)'
    msg_third='Many airports handover to ADANI.......DESH NAHI BIKANE DUNGA (JOKE!!!!)'
    my_dir={'head_msg':head_msg,'msg_first':msg_first,'msg_second':msg_second,'msg_third':msg_third}
    return render(request,'newsapp/news.html',context=my_dir)
