from .models import Record
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView,DeleteView,FormView
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView,FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

class RecordListView(ListView):
    model = Record  
    context_object_name = 'record'
    template_name = 'work_list.html'
    ordering = ['-id']


class RecordDetailView(DetailView):
    model = Record
    context_object_name = 'record' 
    template_name = 'work_detail.html' 


class RecordCreateView(CreateView):
    model = Record
    fields = ['title','content','date']
    template_name = 'work_form.html' 

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RecordCreateView,self).form_valid(form)


class RecordUpdateView(UpdateView):
    model = Record
    fields = ['title','content','date']
    
    template_name = 'work_form.html' 


class RecordDeleteView(DeleteView):
    model = Record
    fields = '__all__'

    template_name = 'work_form.html' 
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(workcreate,self).form_valid(form)