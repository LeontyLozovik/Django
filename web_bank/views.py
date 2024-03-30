from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import *

from web_bank.forms import RegisterUserForm, LoginUserForm


# Create your views here.

def index(r):
    return render(r, 'index.html')


class Persons(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'persons.html'
    context_object_name = 'persons'
    paginate_by = 2
    login_url = '/login/'


def products(r, id):
    if id:
        product = Product.objects.get(id=id)
        return render(r, 'product.html', {'product': product})
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page_num = r.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(r, 'products.html', {'products': products, 'page_obj': page_obj})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'form_reg_user.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'form_login_user.html'

    def get_success_url(self) -> str:
        return reverse_lazy('index')


def logout_user(r):
    logout(r)
    return redirect('login')
