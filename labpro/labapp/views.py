from django.shortcuts import render, redirect
from django.views import generic
from .forms import *
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.models import User
import os
from django.shortcuts import render
from labpro.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request,"index.html")
def user_index(request):
    return render(request,"user_index.html")

def registration(request):
    if request.method=='POST':
        a=regform(request.POST)
        if a.is_valid():
            fn=a.cleaned_data['fullname']
            un=a.cleaned_data['username']
            em=a.cleaned_data['email']
            ph=a.cleaned_data['phone']
            g=a.cleaned_data['gender']
            ps=a.cleaned_data['password']
            cs=a.cleaned_data['cpassword']
            b=regmodel(fullname=fn,username=un,email=em,phone=ph,gender=g,password=ps)

            if ps==cs:
                b.save()
                return redirect(login)
            else:
                return HttpResponse('registration failed')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        x=logform(request.POST)
        if x.is_valid():
            un=x.cleaned_data['username']
            ps=x.cleaned_data['password']
            y=regmodel.objects.all()
            for i in y:
                if un==i.username and ps==i.password:

                    return render(request,'admin_index.html')
            else:
                return HttpResponse("login failed")
    else:
        return render(request,'admin_login.html')

def userreg(request):
    if request.method == 'POST':
        a = userregform(request.POST)
        if a.is_valid():
            fn = a.cleaned_data['fullname']
            un = a.cleaned_data['username']
            em = a.cleaned_data['email']
            ph = a.cleaned_data['phone']
            g = a.cleaned_data['gender']
            ps = a.cleaned_data['password']
            cs = a.cleaned_data['cpassword']
            b = userregmodel(fullname=fn, username=un, email=em, phone=ph, gender=g, password=ps)

            if ps == cs:
                b.save()
                return redirect(userlogin)
            else:
                return HttpResponse('registration failed')
    else:
        return render(request, 'register.html')


def userlogin(request):
    if request.method == 'POST':
        x = userlogform(request.POST)
        if x.is_valid():
            un = x.cleaned_data['username']
            ps = x.cleaned_data['password']
            y = userregmodel.objects.all()
            for i in y:
                if un == i.username and ps == i.password:
                    return HttpResponse("login sucessfull")
            else:
                return HttpResponse("login failed")
    else:
        return render(request, 'login.html')


def appo(request,id):
    a=services_model.objects.get(id=id)

    if request.method=='POST':
        x=apointform(request.POST)
        if x.is_valid():
            ab = x.cleaned_data['name']
            ac = x.cleaned_data['email']
            ad = x.cleaned_data['date']
            ae = x.cleaned_data['time']
            af = x.cleaned_data['department']
            ag=x.cleaned_data['price']
            b=apoint(name=ab,email=ac,date=ad,time=ae,department=af,price=ag)
            b.save()
            return render(request,'appoinment show.html',{'ab':ab,'ac':ac,'ad':ad,'ae':ae,'af':af,'ag':ag})
        else:
            return HttpResponse("appoinment failed")
    else:
        return render(request,'apoinment.html',{'a':a,})

# def show(request,id):
#     a=services_model.objects.get(id=id)
#
#     if request.method=='POST':
#         x=apointform(request.POST)
#         if x.is_valid():
#             ab = x.cleaned_data['name']
#             ac = x.cleaned_data['email']
#             ad = x.cleaned_data['date']
#             ae = x.cleaned_data['time']
#             af = x.cleaned_data['department']
#             b=apoint(name=ab,email=ac,date=ad,time=ae,department=af)
#             b.save()
#             return HttpResponse("appoinment taken succesfull")
#         else:
#             return HttpResponse("appoinment failed")
#     else:
#         return render(request,'apoinment.html',{'a':a})

def appoint(request):
    a=apoint.objects.all()
    return render(request,'show_appoinment.html',{'a':a})


def userdetails(request):
    a=userregmodel.objects.all()
    return render(request,'user_details.html',{'a':a})

#
# def apointdisplay(request):
#    x=apoint.objects.all()
#    nam=[]
#    emai=[]
#    dat = []
#    tim=[]
#    dept=[]
#    id=[]
#
#    for i in x:
#        nm=i.name
#        nam.append(nm)
#        em=i.email
#        emai.append(em)
#        dt=i.date
#        dat.append(dt)
#        tm = i.time
#        tim.append(tm)
#        dep = i.department
#        dept.append(dep)
#        id1=i.id
#        id.append(id1)
#    mylist=zip(nam,emai,dat,tim,dept,id)
#    return render(request,'show_appoinment.html',{'mylist':mylist})



def userprofile(request):
    a=userregmodel.objects.all()
    for i in a:
        uname=i.username
        em=i.email
    return render(request,'user_index.html',{'uname':uname,'em':em})


def pay(request,ag):
    a=ag
    if request.method=='POST':
        x=paymentform(request.POST)
        if x.is_valid():
            ab = x.cleaned_data['cardnumber']
            ac = x.cleaned_data['cvv']
            ad = x.cleaned_data['exp_date']
            # ae = x.cleaned_data['card_holder_name']
            af=x.cleaned_data['amount']
            ah=x.cleaned_data['email_id']
            b=paymentmodel(cardnumber=ab,cvv=ac,exp_date=ad,amount=af,email_id=ah)
            b.save()
            # message="your payment is successfull and you APoinment has booked"
            # send_mail(str('MDC LABARORATRY')  +'||' +str(ag),message,EMAIL_HOST_USER,[ah],fail_silently=False)
            return HttpResponse("payment succesfull")
        else:
            return HttpResponse("payment failed")
    else:
        return render(request,'payment.html',{'a':a})

def adminindex(request):
    return render(request,"admin_index.html")


def serviceadd(request):
    if request.method=='POST':
        a=addservices(request.POST,request.FILES)
        if a.is_valid():
            nm=a.cleaned_data['testname']
            np=a.cleaned_data['test_desc']
            de=a.cleaned_data['test_price']
            im=a.cleaned_data['test_image']
            b=services_model(testname=nm,test_desc=np,test_price=de,test_image=im)
            b.save()
            return redirect(servicedisplay)
        else:
            return HttpResponse("file upload failed")
    else:
        return render(request,"add_services.html")

def servicedisplay(request):
   x=services_model.objects.all()
   li=[]
   item=[]
   price = []
   des1=[]
   id=[]

   for i in x:
       path=i.test_image
       li.append(str(path).split("/")[-1])
       nm=i.testname
       item.append(nm)
       pri=i.test_price
       price.append(pri)
       dis=i.test_desc
       des1.append(dis)
       id1 = i.id
       id.append(id1)

   mylist=zip(li,item,price,des1,id)
   return render(request,'services_display.html',{'mylist':mylist})

def service_edit(request):
   x=services_model.objects.all()
   li=[]
   item=[]
   price = []
   des1=[]
   id=[]

   for i in x:
       path=i.test_image
       li.append(str(path).split("/")[-1])
       nm=i.testname
       item.append(nm)
       pri=i.test_price
       price.append(pri)
       dis=i.test_desc
       des1.append(dis)
       id1 = i.id
       id.append(id1)

   mylist=zip(li,item,price,des1,id)
   return render(request,'edit_services.html',{'mylist':mylist})


def edit_service(request,id):
    prod=services_model.objects.get(id=id)
    li=str(prod.test_image).split('/')[-1]
    if request.method =="POST":
        if len(request.FILES) != 0:
            if len(prod.test_image) > 0:
                os.remove(prod.test_image.path)
            prod.test_image=request.FILES['test_image']
        prod.testname=request.POST.get('testname')
        prod.test_desc=request.POST.get('test_desc')
        prod.test_price=request.POST.get('test_price')
        prod.save()
        return redirect(service_edit)
    context={'prod':prod,'li':li}
    return render(request,'edit.html',context)

def delete(request,id):
    prod=services_model.objects.get(id=id)
    if len(prod.test_image) > 0:
        os.remove(prod.test_image.path)
    prod.delete()
    return redirect(servicedisplay)






