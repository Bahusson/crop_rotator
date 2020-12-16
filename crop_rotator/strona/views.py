from django.shortcuts import (render, redirect, get_object_or_404 as G404)
from django.contrib.auth.models import User  # Zaimportuj uproszczony model usera.
from .models import (PageSkin as S,  PageNames as P, RegNames, AboutPageNames)
from rotator.models import (RotationPlan)
from crop_rotator.settings import LANGUAGES as L
from meetap.core.classes import (PageElement as pe, PageLoad)


# Widok strony domowej.
def home(request):
    context = {
     'rotation_plans': RotationPlan,
     }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/home.html'
    return render(request, template, context_lazy)


# Widok "O programie" - W_I_P, do zmiany?
def about(request):
    context = {
     'about_us': AboutPageNames,
     }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S)
    template = 'strona/home.html'
    return render(request, template, context_lazy)


# Widok wszystkich płodozmianów - W_I_P, ale właściwie to tak zostanie. ;)
def allplans(request):
    context = {
     'rotation_plans': RotationPlan,
     }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/home.html'
    return render(request, template, context_lazy)
