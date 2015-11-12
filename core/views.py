from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import *

# Create your views here.

class Home(TemplateView):
  template_name = "home.html"

class ClassCreateView(CreateView):
  model = Class
  template_name = "class/class_form.html"
  fields = ['course', 'professor']
  success_url = reverse_lazy('home')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(ClassCreateView, self).form_valid(form)