from django.shortcuts import render
from .forms import addim
from .models import addimg, addimg1
from django.shortcuts import  render,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout


def home(request):
    return render(request,'home.html')

def add_image(request):
    if request.method=='POST':
        ab = addim(request.POST,request.FILES)
        if ab.is_valid():
            ad = ab.cleaned_data['im']
            bc = ab.cleaned_data['is_pri']
            bc = addimg1(im=ad,is_pri = bc)
            bc.save()
            return HttpResponseRedirect('/')
    else:
        ab = addim()
        abc = addimg1.objects.all().filter(is_pri = False).order_by('-id')
        return render(request,'add_image.html',{'nam':'ADD IMAGE','form':ab,'image':abc})
    
def private_image(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/') 
    ab = addimg1.objects.all().filter(is_pri = True)
    return render(request,'utilities.html',{'image':ab})

def user_login(request):
    if  request.user.is_authenticated:
         return HttpResponseRedirect('/private/')
    if request.method == "POST":
        fm = AuthenticationForm(request=request ,data = request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            print(uname,upass)
            user = authenticate(username = uname, password =upass )
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/private/')
        else:
            messages.success(request,'you are not a valid user')
    else:
        fm = AuthenticationForm()
    return render(request,'login.html',{'form':fm,'nam':'LOGIN'})


"""
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        return HttpResponseRedirect('/login/')

def add_image(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/') 
    
    if request.method=='POST':
        ab = addim(request.POST,request.FILES)
        if ab.is_valid():
            ad = ab.cleaned_data['im']
            bc = addimg(im=ad)
            bc.save()
            return HttpResponseRedirect('/')
    else:
        ab = addim()
        abc = addimg.objects.all()
        return render(request,'add_image.html',{'nam':'ADD IMAGE','form':ab,'image':abc})

def user_login(request):
    if request.user.is_authenticated:
         return HttpResponseRedirect('/')
    if request.method == "POST":
        fm = AuthenticationForm(request=request ,data = request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            print(uname,upass)
            user = authenticate(username = uname, password =upass )
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/')
        else:
            messages.success(request,'you are not a valid user')
    else:
        fm = AuthenticationForm()
    return render(request,'login.html',{'form':fm,'nam':'LOGIN'})

#login completed

# logout

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        messages.success(request,'First login the page !!')
        return HttpResponseRedirect('/login/')
"""
