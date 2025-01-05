from django.shortcuts import render,redirect
from .forms import LoginForm, CreateUserForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate


# Create your views here.

# - Home Page
def home(request):
    # return HttpResponse("Hello world")
    return render(request,"webapp/index.html")


# - Register a user
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    context = {'form':form}
    return render(request,'webapp/register.html',context)
            


# - Login a user
def login_user(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)

            if user is not None:
                auth.login(request,user)
                # return redirect('')

    context = {'form':form }
    return render(request,'webapp/my-login.html',context)



# - Dashboard of a user




# - Logout a user        
def logout_user(request):
    auth.logout(request)
    return redirect('login')

    