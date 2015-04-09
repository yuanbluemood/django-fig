from django.shortcuts import render
from .forms import EmailForm
# from .models import Join

def home(request):
	# print request.POST
	# form = EmailForm(request.POST or None)
	# if form.is_valid():
	# 	email= form.cleaned_data['email']
	Context = ''
	# Context = {'form':form}
	#messages.add_message(request, messages.SUCCESS, 'Hello world.')
	return render(request,'home.html',Context)


def overview(request):
	Context = ''
	#messages.add_message(request, messages.SUCCESS, 'Hello world.')
	return render(request,'overview.html',Context)

def myapp(request):
	Context = ''
	#messages.add_message(request, messages.SUCCESS, 'Hello world.')
	return render(request,'myapp.html',Context)

def myservice(request):
	Context = ''
	#messages.add_message(request, messages.SUCCESS, 'Hello world.')
	return render(request,'myservice.html',Context)