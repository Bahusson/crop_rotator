from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from strona.models import PageNames as P, PageSkin as S, RegNames
from crop_rotator.settings import LANGUAGES as L
from core.classes import PageLoad
from django.contrib.auth.forms import AuthenticationForm
from .forms import ExtendedCreationForm
from core.snippets import gen_login


# Formularz rejestracji.
def register(request):
    if request.method == "POST":
        form = ExtendedCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            # Sprawdza shaszowane dane powyżej w bazie danych.
            login(request, user)
            return redirect("home")
            # Przekierowuje na stronę główną zalogowanego usera.
    else:
        my_username = gen_login()
        form = ExtendedCreationForm()
        locations = list(RegNames.objects.all())
        item = locations[0]
        context = {
            "gen_username": my_username,
            "form": form,
            "item": item,
        }
        pl = PageLoad(P, L)
        context_lazy = pl.lazy_context(skins=S, context=context)
        template = "registration/register.html"
        return render(request, template, context_lazy)


# Formularz logowania.
def logger(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")

    else:
        form = AuthenticationForm()
    locations = list(RegNames.objects.all())
    item = locations[0]
    context = {
        "form": form,
        "item": item,
    }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(skins=S, context=context)
    template = "registration/login.html"
    return render(request, template, context_lazy)
