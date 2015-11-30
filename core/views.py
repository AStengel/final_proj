from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import *
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.views.generic import FormView
from .forms import *

# Create your views here.

class Home(TemplateView):
  template_name = "home.html"

class CourseCreateView(CreateView):
  model = Course
  template_name = "course/course_form.html"
  fields = ['course', 'professor']
  success_url = reverse_lazy('course_list')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(CourseCreateView, self).form_valid(form)
class CourseListView(ListView):
  model = Course
  template_name = "course/course_list.html"

class CourseDetailView(DetailView):
  model = Course
  template_name = 'course/course_detail.html'

  def get_context_data(self, **kwargs):
    context = super(CourseDetailView, self).get_context_data(**kwargs)
    course = course.objects.get(id=self.kwargs['pk'])
    notes = Note.objects.filter(course=course)
    context['notes'] = notes
    user_notes= Note.objects.filter(course=course, user=self.request.user)
    context['user_notes'] = user_notes
    return context

class CourseUpdateView(UpdateView):
  model = Course
  template_name = 'course/course_form.html'
  fields = ['class', 'professor']

  def get_object(self, *args, **kwargs):
    object = super(CourseUpdateView, self).get_object(*args, **kwargs)
    if object.user !=self.request.user:
      raise PermissionDenied()
    return object

class CourseDeleteView(DeleteView):
  model = Course
  template_name = 'course/course_confirm_delete.html'
  success_url = reverse_lazy('course_list')

  def get_object(self, *args, **kwargs):
    object = super(CourseDeleteView, self).get_object(*args, **kwargs)
    if object.user !=self.request.user:
      raise PermissionDenied()
    return object

class NoteCreateView(CreateView):
  model = Note
  template_name = "note/note_form.html"
  fields = ['note']

  def get_success_url(self):
    return self.object.question.get_absolute_url()

  def form_valid(self, form):
    form.instance.user = self.request.user
    form.instance.course = course.objects.get(id=self.kwargs['pk'])
    return super(NoteCreateView, self).form_valid(form)

    course= course.objects.get(id=self.kwargs['pk'])
    if Note.objects.filter(course=course, user=self.request.user).exists():
      raise PermissionDenied()



class NoteUpdateView(UpdateView):
  model = Note
  pk_url_kwarg = 'note_pk'
  template_name = 'note/note_form.html'
  fields = ['text']

  def get_success_url(self):
    return self.object.question.get_absolute_url()

  def get_object(self, *args, **kwargs):
    object = super(NoteUpdateView, self).get_object(*args, **kwargs)
    if object.user !=self.request.user:
      raise PermissionDenied()
    return object

class NoteDeleteView(DeleteView):
  model = Note
  pk_url_kwarg = 'note_pk'
  template_name = 'note/note_confirm_delete.html'

  def get_success_url(self):
    return self.object.course.get_absolute_url()

  def get_object(self, *args, **kwargs):
    object = super(NoteDeleteView, self).get_object(*args, **kwargs)
    if object.user !=self.request.user:
      raise PermissionDenied()
    return object

class VoteFormView(FormView):
  form_class = VoteForm

  def form_valid(self, form):
    user = self.request.user
    course = Course.objects.get(pk=form.data["course"])
    try:
      note = Note.objects.get(pk=form.data["note"])
      prev_votes = Vote.objects.filter(user=user, note=note)
      has_voted = (prev_votes.count()>0)
      if not has_voted:
        Vote.objects.create(user=user, note=note)
      else:
        prev_votes[0].delete()
      return redirect(reverse('course_detail', args=[form.data["course"]]))
    except:
      prev_votes = Vote.objects.filter(user=user, course=course)
      has_voted = (prev_votes.count()>0)
      if not has_voted:
        Vote.objects.create(user=user, course=course)
      else:
        prev_votes[0].delete()
    return redirect('course_list')
  
class UserDetailView(DetailView):
  model = User
  slug_field = 'username'
  template_name = 'user/user_detail.html'
  context_object_name = 'user_in_view'
  
  def get_context_data(self, **kwargs):
    context = super(UserDetailView, self).get_context_data(**kwargs)
    user_in_view = User.objects.get(username=self.kwargs['slug'])
    courses = Course.objects.filter(user=user_in_view)
    context['courses'] = courses
    notes = Note.objects.filter(user=user_in_view)
    context['notes'] = notes
    return context
  
class UserUpdateView(UpdateView):
  model = User
  slug_filed = "username"
  template_name = "user/user_form.html"
  fields = ['email', "first_name", 'last_name']
  
  def get_success_url(self):
    return reverse('user_detail', args=[self.request.user.username])
  
  def get_object(self, *args, **kwargs):
    object = super(UserUpdateView, self).get_object(*args, **kwargs)
    if object != self.request.user:
      raise PermissionDenied()
    return object
  
class UserDeleteView(DeleteView):
  model = User
  slug_field = "username"
  template_name = 'user/user_confirm_delete.html'
  
  def get_success_url(self):
    return reverse_lazy('logout')
  
  def get_object(self, *args, **kwargs):
    object = super(UserDeleteView, self).get_object(*args, **kwargs)
    if object != self.request.user:
      raise PermissionDenied()
    return object
  
  def delete(self, request, *args, **kwargs):
    user = super(UserDeleteView, self).get_object(*args)
    user.is_active = False
    user.save()
    return redirect(self.get_success_url())
  
class SearchCourseListView(CourseListView):
  def get_queryset(self):
    incoming_query_string = self.request.GET.get('query', '')
    return Course.objects.filter(title__icontains=incoming_query_string)

