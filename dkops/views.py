from django.shortcuts import render
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from .forms import EmailForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# from .models import Join

@login_required(login_url='/login/')
def home(request):
	# print request.POST
	# form = EmailForm(request.POST or None)
	# if form.is_valid():
	# 	email= form.cleaned_data['email']
	Context = ''
	# Context = {'form':form}
	#messages.add_message(request, messages.SUCCESS, 'Hello world.')
	return render(request,'home.html',Context)


@login_required(login_url='/login/')
def overview(request):
	Context = ''
	#messages.add_message(request, messages.SUCCESS, 'Hello world.')
	return render(request,'overview.html',Context)

@login_required(login_url='/login/')
def myapp(request):
	Context = ''
	#messages.add_message(request, messages.SUCCESS, 'Hello world.')
	return render(request,'myapp.html',Context)

@login_required(login_url='/login/')
def myservice(request):
	Context = ''
	#messages.add_message(request, messages.SUCCESS, 'Hello world.')
	return render(request,'myservice.html',Context)

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if not request.POST.get('remember-me',None):
            print "checked remember-me"
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    return render_to_response('login.html', context_instance=RequestContext(request))

