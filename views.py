from django.shortcuts import render,redirect

from . import forms
from .models import techer,Contact,student
from .forms import studentform
# Create your views here.

def index(request):
   return render(request,'index.html')


def teacher(request):
    myposts = techer.objects.all()
    print(myposts)
    return render(request, 'teachers.html',
                  {'myposts': myposts})

def contact(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'contact.html', {'thank': thank})


def register(request):
    if request.method == 'POST':
        frm = studentform(request.POST)
        if frm.is_valid():
            username = request.POST['userid']
            if student.objects.filter(userid=username):
                raise forms.ValidationError('User All Ready Exist')

            frm.save()
            return redirect("/regsuccess")
    else:
        frm = studentform()
    return render(request, 'reg.html', {'stu': frm})


def success(request):
    return render(request, 'success.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['userid']
        password = request.POST['passwd']
        try:
            # user = auth.authenticate(userid=username,passwd=password)
            record = student.objects.get(userid=username, passwd=password)

            # print(record)
            if record is not None:
                # auth.login(request,user)
                return redirect('/loginsuccess')
            else:
                return redirect('/invalid')
        except:

            return redirect('/invalid')
    else:
        frm = studentform()
    return render(request, 'login.html', {'stu': frm})


def logsuc(request):
    return render(request, 'loginsuccess.html')


def loginvalid(request):
    return render(request, 'invalid.html')
