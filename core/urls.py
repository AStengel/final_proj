from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
   url(r'^$', Home.as_view(), name='home'),
   url(r'^user/', include('registration.backends.simple.urls')),
   url(r'^user/', include('django.contrib.auth.urls')), 
   url(r'^class/create/$', ClassCreateView.as_view(), name='class_create'),   
   url(r'question/$', ClassListView.as_view(), name='class_list'),   
   url(r'^class/(?P<pk>\d+)/$', ClassDetailView.as_view(), name='class_detail'),  
   url(r'^class/update/(?P<pk>\d+)/$', ClassUpdateView.as_view(), name='class_update')                    
)                       