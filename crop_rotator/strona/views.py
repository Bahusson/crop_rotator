from django.shortcuts import (render, redirect, get_object_or_404 as G404)
from django.contrib.auth.models import User  # Zaimportuj uproszczony model usera.
from .models import (PageSkin as S,  PageNames as P, RegNames, AboutPageNames)
from rotator.models import (RotationPlan, RotationStep)
from crop_rotator.settings import LANGUAGES as L
from core.classes import (PageElement as pe, PageLoad)
from core.snippets import booleanate as bot, flare


# Widok strony domowej.
def home(request):
    pe_rp = pe(RotationPlan).allelements
    context = {
     'rotation_plans': pe_rp,
     }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/home.html'
    return render(request, template, context_lazy)


# Widok "O programie"
def about(request):
    pe_apn = pe(AboutPageNames).baseattrs
    context = {
     'about_us': pe_apn,
     }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/about.html'
    return render(request, template, context_lazy)


# Widok wszystkich płodozmianów - dodać wyszukiwarkę?
def allplans(request):
    pe_rp = pe(RotationPlan).allelements
    context = {
     'rotation_plans': pe_rp,
     }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/allplans.html'
    return render(request, template, context_lazy)


# Widok pojedynczego płodozmianu - W_I_P.
def plan(request, plan_id):
    pe_rp = pe(RotationPlan)
    pe_rp_id = pe_rp.by_id(G404=G404, id=plan_id)
    #userdata = User.objects.get(
    # id=request.user.id)
    #user_id = userdata.id
    #flare(user_id)
    #owner_id = pe_rp_id.owner.id
    #flare(owner_id)
    #if user_id == owner_id:
    #    flare("True_af")
    #    pass
    #else:
    #    flare("False_af")
    #    pass
        # return redirect('logger')
    # Zrób jeśli user jest właścicielem, żeby mógł robić zmiany.
    pe_rs = RotationStep.objects.filter(from_plan=plan_id)
    context = {
     'plan': pe_rp_id,
     'steps': pe_rs,
     }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/plan.html'
    return render(request, template, context_lazy)
