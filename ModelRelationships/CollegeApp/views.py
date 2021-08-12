from django.shortcuts import render
from django.db import models
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from .models import Dept
from django.urls import reverse_lazy

# Create your views here.
class DeptCreateView(CreateView):
    model = Dept
    fields = '__all__'
    success_url = reverse_lazy('retrive_dept')

class DeptListView(ListView):
    model = Dept

class DeptUpdateView(UpdateView):
    model = Dept
    fields = '__all__'
    success_url = reverse_lazy('retrive_dept')

class DeptDeleteView(DeleteView):
    model = Dept
    success_url = reverse_lazy('retrive_dept')


