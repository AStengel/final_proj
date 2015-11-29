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

# Create your views here.

class Home(TemplateView):
  template_name = "home.html"

class ClassCreateView(CreateView):
  model = Class
  template_name = "class/class_form.html"
  fields = ['course', 'professor']
  success_url = reverse_lazy('class_list')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(ClassCreateView, self).form_valid(form)
class ClassListView(ListView):
  model = Class
  template_name = "class/class_list.html"

class ClassDetailView(DetailView):
  model = Class
  template_name = 'class/class_detail.html'

  def get_context_data(self, **kwargs):
    context = super(ClassDetailView, self).get_context_data(**kwargs)
    Class = Class.objects.get(id=self.kwargs['pk'])
    notes = Note.objects.filter(Class=Class)
    context['notes'] = notes
    return context

class ClassUpdateView(UpdateView):
  model = Class
  template_name = 'class/class_form.html'
  fields = ['class', 'professor']
  
  def get_object(self, *args, **kwargs):
    object = super(ClassUpdateView, self).get_object(*args, **kwargs)
    if object.user !=self.request.user:
      raise PermissionDenied()
    return object

class ClassDeleteView(DeleteView):
  model = Class
  template_name = 'class/class_confirm_delete.html'
  success_url = reverse_lazy('class_list')
  
  def get_object(self, *args, **kwargs):
    object = super(ClassDeleteView, self).get_object(*args, **kwargs)
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
    form.instance.Class = Class.objects.get(id=self.kwargs['pk'])
    return super(NoteCreateView, self).form_valid(form)

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
    return self.object.Class.get_absolute_url()

  def get_object(self, *args, **kwargs):
    object = super(NoteDeleteView, self).get_object(*args, **kwargs)
    if object.user !=self.request.user:
      raise PermissionDenied()
    return object