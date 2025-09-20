from django.contrib.auth import login,logout
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserForm,UpdateUser,UpdateProfile
from django.contrib.auth.forms import AuthenticationForm
from .middleware import auth,guest
from store.models import Profile,ProfileUser
# Create your views here.
@guest
def Register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registered successfully!")
              # Automatically log in the user after registration
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, 'User/register.html', context)
   
@guest
def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            # Authenticate and log in the user
            users = form.get_user()
            login(request, users)
            messages.success(request,"logged in successfully!")
            return redirect('/') 
            # Redirect to a success page
    else:
        form = AuthenticationForm()
    
    return render(request, 'User/login.html', {'form': form})

def Logout(request):
    logout(request)
    messages.success(request,"logged out successfully!")
    return redirect('login')

def Profile_View(request):
    if request.method == "POST":
        u_form = UpdateUser(request.POST or None,instance=request.user)
        p_form = UpdateProfile(request.POST or None,request.FILES or None,instance = request.user.profileuser)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect("profile")
    else:
        u_form = UpdateUser(instance=request.user)
        p_form = UpdateProfile(instance=request.user.profileuser)

    profile = Profile.objects.filter(user=request.user).first()
    context={
        'u_form':u_form,
        'profile':profile,
        'p_form':p_form
    }
    return render(request,'User/profile.html',context)
