#Dir for snippets
#C:\Users\Jeanne\AppData\Roaming\Sublime Text 3\Packages\User

from django.shortcuts import render
#from . import forms

# Create your views here.

def index(request):
	context_dict = {'text':'hello world','number':100}
	# change app_names below and see HTML names!
	return render(request,'basic_app/index.html',context_dict)

def other(request):
	# change app_names below and see HTML names!
	return render(request,'basic_app/other.html')

def relative(request):
	# change app_names below and see HTML names!
	return render(request,'basic_app/relative_url_templates.html')

# Now that the views.py is setup, 
# Go to urls.py in basicforms (in the project) and POINT URLS in the right way...