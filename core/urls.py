from django.conf.urls import patterns, include, url
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
   url(r'^$', Home.as_view(), name='home'),
   url(r'^user/', include('registration.backends.simple.urls')),
   url(r'^user/', include('django.contrib.auth.urls')),
   url(r'^course/create/$', login_required(CourseCreateView.as_view()), name='course_create'),
   url(r'course/$', login_required(CourseListView.as_view()), name='course_list'),
   url(r'^course/(?P<pk>\d+)/$', login_required(CourseDetailView.as_view()), name='course_detail'),
   url(r'^course/update/(?P<pk>\d+)/$', login_required(CourseUpdateView.as_view()), name='course_update'),
   url(r'^course/delete/(?P<pk>\d+)/$', login_required(CourseDeleteView.as_view()), name='course_delete'),
   url(r'^course/(?P<pk>\d+)/note/create/$', login_required(NoteCreateView.as_view()), name='note_create'),
   url(r'^course/(?P<course_pk>\d+)/note/update/(?P<note_pk>\d+)/$', login_required(NoteUpdateView.as_view()), name='note_update'),
   url(r'^course/(?P<course_pk>\d+)/note/delete/(?P<note_pk>\d+)/$', login_required(NoteDeleteView.as_view()), name='note_delete'),
   url(r'^vote/$', login_required(VoteFormView.as_view()), name='vote'),
   url(r'^user/(?P<slug>\w+)/$', login_required(UserDetailView.as_view()), name='user_detail'),
   url(r'^user/update/(?P<slug>\w+)/$', login_required(UserUpdateView.as_view()), name='user_update'),
   url(r'^user/delete/(?P<slug>\w+)/$', login_required(UserDeleteView.as_view()), name='user_delete'),
)