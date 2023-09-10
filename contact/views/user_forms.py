from django.shortcuts import render, redirect
from django.urls import reverse
from contact.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout


def register(request):
    form = RegisterForm()
    form_action = reverse('contact:register')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso')
            return redirect('contact:index')

    context = {
        'form': form,
        'form_action': form_action,
    }

    return render(request, 'contact/register.html', context)


def login_view(request):
    form = AuthenticationForm(request)
    form_action = reverse('contact:login')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Logado com sucesso')
            return redirect('contact:index')

    context = {
        'form': form,
        'form_action': form_action,
    }

    return render(request, 'contact/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('contact:login')
