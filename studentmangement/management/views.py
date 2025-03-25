from django.shortcuts import render,redirect
from management.models import Student
from django.shortcuts import render
from django. contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        user = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        obj  = User(first_name = name,last_name = last_name,username = user, email = email)
        obj.set_password(password)
        obj.save()
        return redirect('login')
        
    return render(request,'register.html')


def login_user(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        conpassword = request.POST.get('conpassword')
        if password == conpassword:
            obj = authenticate(request,username = name,password = password)
            if obj is not None:
                login(request,obj)
                return redirect('home')
            else:
                return HttpResponse(f"User not found  Please Register !!!!!!")
        else:
            return HttpResponse("Password does not match")
    return render(request,'login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def home(request):

    data = Student.objects.filter(fk = request.user)

    print(data)
    con = {
        'data' : data
    }
    return render(request,'home.html',context=con)




def update(request,pk):
    data = Student.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        data.name = name
        data.age = age
        data.contact = contact
        data.email = email
        data.save()
        return redirect('home')

    studet_data = {
        'data' : data
    }

    return render(request,'update.html',context=studet_data)

def delete(request,pk):
    data = Student.objects.get(id=pk)
    data.delete()
    return redirect('home')
@login_required
def add(request):
    if request.method == 'POST':
    
        name = request.POST.get('name')
        age = request.POST.get('age')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        Student.objects.create(fk = request.user,name=name,age=age,contact=contact,email=email)
        return redirect('home')
    return render(request,'insert.html')
