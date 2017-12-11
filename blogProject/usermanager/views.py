from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def register(request):
	return render(request, 'usermanager/register.html',context={'form':RegisterForm()})

def login(request):
	if (request.session.get('username', False)):
		return redirect('/')
	return render(request, 'usermanager/login.html', context={'form':LoginForm()})

def registerapi(request):
	if(request.method == 'POST'):
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		password2 = request.POST.get('password2', '')
		email = request.POST.get('email', '')
		obj = RegisterForm(request.POST)
		if obj.is_valid:
			if password != password2 or User.objects.filter(username = username).count() != 0 or User.objects.filter(email = email).count() != 0 :
				return render(request, 'usermanager/register.html', context={'form':obj})
		user = User()
		user.username = username
		user.email = email
		user.set_password(password)
		user.save()
		if (not request.session.get('username', False)):		
			newUser=authenticate(username=username,password=password)
			if newUser is not None:  
				request.session['username'] = username  
				request.session.set_expiry(60)  
		return redirect('/')	
	return render(request, 'usermanager/register.html', context={'form': RegisterForm()})

def loginapi(request):
	if request.method == 'POST':
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		obj = LoginForm(request.POST)
		user = authenticate(username=username,password=password)
		if user:
			request.session['username'] = username  
			request.session.set_expiry(60)  
			return redirect('/')
		return render(request, 'usermanager/login.html', context={'form':obj})		
	return render(request, 'usermanager/login.html', context={'form':LoginForm()})

