from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from home.models import Product


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request,'signup.html', {'error':'username already taken'})
            except User.DoesNotExist:
                user =  User.objects.create_user(username =request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'signup.html', {'error': 'password doesnot match'})
    else:
            return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'Invalid username or password'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    else:
        return redirect('login')

@login_required
def userx(request):
    product = Product.objects.filter(creator = request.user)
    pro = Product.objects.raw('SELECT * FROM home_product ORDER BY upvote  DESC LIMIT 3 ')
    return render(request,'user.html',{'product':product,'pro':pro})

