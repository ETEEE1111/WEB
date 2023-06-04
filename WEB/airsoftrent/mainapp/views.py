from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import Authorisation

from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy, reverse
from .forms import AuthUserForm, LoginForm

# class MyProjectLoginView(LoginView):
#     template_name = 'mainapp/autho.html'
#     form_class = AuthUserForm

#     success_url = reverse_lazy('manager')

#     def get_success_url(self):
#         return self.success_url

def MyProjectLoginView(request):
    s = Authorisation.objects.all()
    return render(request, 'mainapp/autho.html', {'s': s})


def auth(request):
    
    return render(request, 'mainapp/autho.html')

def manager(request):
    return render(request, 'mainapp/mng.html')

def add_manger(request):
    return render(request, 'mainapp/add-offer.html')

def change_manager(request):
    return render(request, 'mainapp/change-offer.html')

def marketer(request):
    return render(request, 'mainapp/marketer.html')

def add_marketer(request):
    return render(request, 'mainapp/add-servicer.html')

def change_marketer(request):
    return render(request, 'mainapp/change-servicer.html')

def admin(request):
    return render(request, 'mainapp/adm.html')

def admin_add(request):
    return render(request, 'mainapp/adm-add.html')

def admin_inst(request):
    return render(request, 'mainapp/adm-inst.html')

def admin_mark(request):
    return render(request, 'mainapp/adm-mark.html')

def admin_pol(request):
    return render(request, 'mainapp/adm-pol.html')

def admin_eqp(request):
    return render(request, 'mainapp/adm-eqp.html')

def admin_auth(request):
    return render(request, 'mainapp/adm-auth.html')