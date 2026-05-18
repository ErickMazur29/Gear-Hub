from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from accounts.models import Profile
from accounts.forms import RegisterForm

#Registro de usuario
class Register(CreateView):
    model = Profile
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


#Login de usuario
class Login(LoginView):
    model = Profile
    template_name = 'login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('products_list')
    
def logout_view(request):
    logout(request)
    return redirect ('products_list')

class ProfileDetails(DetailView):
    model = Profile
    template_name = 'profile_detail.html'
    context_object_name = 'profile'