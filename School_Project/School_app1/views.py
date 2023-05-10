from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from School_app1.models import UserInfo
from .models import UserInfo

# from .models import Department, Course

# Create your views here.


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return render (request,'details.html')
        else:
            messages.info(request,"invalid username or password")
            return redirect('login')
    return render(request, "login.html")

def register(request,):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username exist")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect('register')

        return redirect('/')

    return render(request, "register.html")





def details(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        department = request.POST.get('department')
        course = request.POST.get('course')
        purpose = request.POST.get('purpose')
        materials = request.POST.getlist('materials')

        userinfo = UserInfo(name=name, dob=dob, age=age, gender=gender,
                            phone_number=phone_number, email=email, address=address,
                            department=department, course=course, purpose=purpose,
                            materials=materials)
        userinfo.save()

        return HttpResponse('Order Confirmed <br> <a href="/">Return to Home Page</a>')
    else:
        return render(request, 'details.html')

def confirm(request):
    return render(request,"index.html")





