from django.conf.urls import patterns, include, url
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
   url(r'^$', Home.as_view(), name='home'),
   url(r'^user/', include('registration.backends.simple.urls')),
   url(r'^user/', include('django.contrib.auth.urls')),
   url(r'^class/create/$', login_required(ClassCreateView.as_view()), name='class_create'),
   url(r'question/$', login_required(ClassListView.as_view()), name='class_list'),
   url(r'^class/(?P<pk>\d+)/$', login_required(ClassDetailView.as_view()), name='class_detail'),
   url(r'^class/update/(?P<pk>\d+)/$', login_required(ClassUpdateView.as_view()), name='class_update'),
   url(r'^class/delete/(?P<pk>\d+)/$', login_required(ClassDeleteView.as_view()), name='class_delete'),
   url(r'^class/(?P<pk>\d+)/note/create/$', login_required(NoteCreateView.as_view()), name='note_create'),
   url(r'^class/(?P<class_pk>\d+)/note/update/(?P<note_pk>\d+)/$', login_required(NoteUpdateView.as_view()), name='note_update'),
   url(r'^class/(?P<class_pk>\d+)/note/delete/(?P<note_pk>\d+)/$', login_required(NoteDeleteView.as_view()), name='note_delete'),
)