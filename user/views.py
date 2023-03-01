from django.shortcuts import render,redirect
# from django.contrib.auth.forms import registerform
from .forms import registerform,userupdateform,profileupdateform
from django.contrib.auth.models import User
from .models import Profile

def register(request):
    if request.method=='POST':
        reg_form=registerform(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect('Home')
    else:
        reg_form=registerform()
    context={'reg_form':reg_form}
    return render(request,'user/register.html',context)
# Create your views here.

def profile(request):
    return render(request,'user/profile.html',{'user':request.user})

def update(request):
    if request.method=='POST':
        user_form=userupdateform(request.POST,instance=request.user)
        profile_form=profileupdateform(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile-page')
    else:
        user_form=userupdateform(instance=request.user)
        profile_form=profileupdateform(instance=request.user.profile)
    context={
        'user_form':user_form,
        'profile_form':profile_form
    }
    return render(request,'user/update.html',context)