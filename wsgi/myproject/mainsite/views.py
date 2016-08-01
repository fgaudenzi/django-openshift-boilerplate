from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User


def index(request):
    #try:
    #    app=render(request, 'mainsite/index.html', {"page":"index"})
    #except Exception as e:
    #    print e.args


    #flash messages
    #messages.success(request, 'HOME')
    #messages.info(request,'HOME INFO')
    #messages.error(request,'HOME ERROR')
    #messages.warning(request,'HOME WARNiNG')
    return render(request, 'mainsite/index.html', {"page":"index"})

def register(request):
    return render(request, 'mainsite/signup.html', {"page":"register"})


def login(request):
    return render(request, 'mainsite/login.html', {"page":"login"})


def do_register(request):
    print request
    user = User.objects.create_user(request.POST['username'],request.POST['email'] ,request.POST['password'], first_name=request.POST['name'].split(' ')[0], last_name=request.POST['name'].split(' ' )[1] )
    messages.success(request, 'User Created')
    return render(request, 'mainsite/index.html', {"page":"index"})

