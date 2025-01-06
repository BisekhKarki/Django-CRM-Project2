from django.shortcuts import render,redirect
from .forms import LoginForm, CreateUserForm, AddRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required 
from .models import Record
from django.contrib import messages


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
            messages.success(request,"Your account created successfully!!!")
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
            messages.success(request,"Your have been logged in successfully!!!")
            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')

    context = {'form':form }
    return render(request,'webapp/my-login.html',context)



# - Dashboard of a user
@login_required(login_url='login')
def dashboard(request):
    my_records = Record.objects.all()
    context = {'records':my_records}
    return render(request,'webapp/dashboard.html',context)



# Create a record
@login_required(login_url='login')
def create_record(request):
    form = AddRecordForm()
    if request.method == "POST":
        form = AddRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Record created successfully!!!")
            return redirect('dashboard')
    
    context = {'form':form}
    return render(request,'webapp/create-record.html',context)



# Update a record
@login_required(login_url='login')
def update_record(request,pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)

    if request.method == "POST":
        form = UpdateRecordForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record updated successfully!!!")
            return redirect('dashboard')
        
    context = {'form':form}
    return render(request,'webapp/update-record.html',context)


# - Read / View a singular record
@login_required(login_url='login')
def read_record(request,pk):
    all_records = Record.objects.get(id=pk)
    context = {
        'record':all_records
    }
    return render(request,'webapp/view-record.html',context)






# Delete a record
@login_required(login_url='login')
def delete_record(request,pk):
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request,"Record deleted successfully!!!")
    return redirect('dashboard')





# - Logout a user        
def logout_user(request):
    auth.logout(request)
    return redirect('login')

    