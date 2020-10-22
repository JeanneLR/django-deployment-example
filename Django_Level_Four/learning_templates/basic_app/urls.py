# This is the second urls.py which is the one we needed to 
# create inside the app Dir.

from django.conf.urls import url
from basic_app import views # our apps name

# TEMPLATE TAGGING
app_name = 'basic_app' # our apps name

urlpatterns= [
	url(r'^relative/$',views.relative,name='relative'),
	url(r'^other/$',views.other,name='other'),
]