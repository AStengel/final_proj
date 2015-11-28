from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import *
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

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
  
class ClassUpdateView(UpdateView):
  model = Class
  template_name = 'class/class_form.html'
  fields = ['class', 'professor']
  
class ClassDeleteView(DeleteView):
  model = Class
  template_name = 'class/class_confirm_delete.html'
  success_url = reverse_lazy('class_list')
 