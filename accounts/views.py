from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from accounts.models import Profile
from accounts.forms import RegisterForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



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
    
#Logout de usuario
@method_decorator(login_required(login_url='login'), name='dispatch')    
def logout_view(request):
    logout(request)
    return redirect ('products_list')

#Detalhes Perfil de usuario
@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileDetails(DetailView):
    model = Profile
    template_name = 'profile_detail.html'
    context_object_name = 'profile'


#Editar Perfil de usuario
@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileUpdate(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'profile_update.html'
    context_object_name = 'profile_update'
    success_url = '/product_list/'

    def get_success_url(self):
        return reverse_lazy('profile_detail', kwargs={'pk': self.object.pk})
