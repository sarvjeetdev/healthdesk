from .models import Record
from django.shortcuts import render, redirect

class RecordListView(ListView):
    model = Record  
    context_object_name = 'record'
    template_name = 'record.html'
    ordering = ['-id']


class RecordDetailView(DetailView):
    model = Record
    context_object_name = 'record' 
    template_name = 'recorddetails.html' 


class RecordCreateView(LoginRequiredMixin,CreateView):
    model = Record
    fields = ['title','desc','done']
    success_url = reverse_lazy('works')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(workcreate,self).form_valid(form)


class RecordUpdateView(LoginRequiredMixin,UpdateView):
    model = Record
    fields = ['title','desc','done']
    success_url = reverse_lazy('works')



class RecordDeleteView(LoginRequiredMixin,DeleteView):
    model = Record
    fields = '__all__'
    success_url = reverse_lazy('works')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(workcreate,self).form_valid(form)