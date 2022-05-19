from django.db import models

from django.shortcuts import render,redirect
from  django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


from .forms import Register
from .models import Reporting,Profile,Schooling,Units,CName,Upload_Units
from django.urls import reverse

def profile(request):
    context={'prof':Upload_Units.objects.all()}
    
    return render(request,"Users/profile.html",context)


class report(LoginRequiredMixin,CreateView):
    model=Reporting
    template_name='Users/report.html'
    fields=['report']
    def form_valid(self,form):
        form.instance.user = self.request.user
      
        return super().form_valid(form)

class profile(LoginRequiredMixin,ListView):
    model=Profile
    template_name='Users/profile.html'

class update_profile(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Profile
    template_name='Users/update_profile.html'
    fields=['pic','email','f_name','l_name','surname']
    def form_valid(self,form):
        form.instance.user
        return super().form_valid(form)
    def test_func(self):
        detail = self.get_object()
        if self.request.user == detail.user :
            return True
        return False


class runits(LoginRequiredMixin,CreateView):
    model=Units
    template_name='Users/runits.html'
    fields=['unit1','unit2','unit3','unit4','unit5']
    def form_valid(self,form):
        form.instance.user = self.request.user
      
        return super().form_valid(form)
    def get_absolute_url(self):
        return reverse('units')
    
class units(ListView):
    model=Units
    template_name='Users/units.html'

class all_units(ListView):
    model=Upload_Units
    template_name='Users/aunits.html'
    context_object_name='prof'

