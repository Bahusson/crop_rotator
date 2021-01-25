from django.shortcuts import render, redirect, get_object_or_404 as G404
from django.contrib.auth.models import User  # Zaimportuj uproszczony model usera.
from .models import PageSkin as S, PageNames as P, RegNames, AboutPageNames
from rotator.models import (
    RotationPlan,
    RotationStep,
    Crop,
    CropFamily,
    CropDataSource as CDS,
)
from crop_rotator.settings import LANGUAGES as L
from core.classes import PageElement as pe, PageLoad, CropPlanner
from core.snippets import (
    booleanate as bot,
    flare,
    level_off,
    list_appending_short,
    remove_repeating,
    repack,
    check_slaves,
    check_ownership,
)
from django.contrib.auth.decorators import login_required
from rotator.forms import (
    RotationPlanForm,
    FirstRotationStepForm,
    NextRotationStepForm,
    UserPlanPublicationForm
)
from rotator.models import Crop
#import itertools
#import copy
from operator import attrgetter
from random import shuffle


# Widok strony domowej.
def home(request):
    pe_rp = pe(RotationPlan).allelements
    pe_rp_published = pe_rp.filter(published=True)
    pe_rp_shuffled = list(pe_rp_published)
    shuffle(pe_rp_shuffled)  # Losuje z widocznych na głównej.
    context = {
        "rotation_plans": pe_rp_shuffled,
    }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(skins=S, context=context)
    template = "strona/home.html"
    return render(request, template, context_lazy)


# Widok "O programie"
def about(request):
    pe_apn = pe(AboutPageNames).baseattrs
    context = {
        "about_us": pe_apn,
    }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(skins=S, context=context)
    template = "strona/about.html"
    return render(request, template, context_lazy)


# Widok wszystkich płodozmianów - dodać wyszukiwarkę?
def allplans(request):
    pe_rp = pe(RotationPlan).allelements
    pe_rp_published = pe_rp.filter(published=True)
    context = {
        "rotation_plans": pe_rp_published,
    }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(skins=S, context=context)
    template = "strona/allplans.html"
    return render(request, template, context_lazy)


# Widok pojedynczego płodozmianu
def plan(request, plan_id):
    pe_rp = pe(RotationPlan)
    pe_rp_id = pe_rp.by_id(G404=G404, id=plan_id)
    user_editable = False
    if check_ownership(request, User, pe_rp_id):
        user_editable = True
    form = NextRotationStepForm()
    context = {
        "user_editable": user_editable,  # Bramka dla zawartości widocznej tylko dla autora.
        "form": form,
    }
    cp = CropPlanner(pe_rp_id, RotationStep, plan_id=plan_id)
    plans_context = cp.basic_context(context=context)
    # Do przeniesienia dla widoku tylko w wersji dla edytora.
    # Dodaj następny krok do planu
    if "next_step" in request.POST:
        form = NextRotationStepForm(request.POST)
        if form.is_valid():
            form.save(pe_rp_id, top_tier)
            return redirect(request.META.get('HTTP_REFERER'))
    # Usuń cały plan.
    if "delete_plan" in request.POST:
        pe_rp_id.delete()
        return redirect('my_plans')
    if "publish_plan" in request.POST:
        form = UserPlanPublicationForm(request.POST, instance=pe_rp_id)
        if form.is_valid():
            form.save(True)
            return redirect(request.META.get('HTTP_REFERER'))
    if "unpublish_plan" in request.POST:
        form = UserPlanPublicationForm(request.POST, instance=pe_rp_id)
        if form.is_valid():
            form.save(False)
            return redirect(request.META.get('HTTP_REFERER'))
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(skins=S, context=plans_context)
    template = "strona/plan.html"
    return render(request, template, context_lazy)


# Widok szczegółowy pojedynczego gatunku - W_I_P
def crop(request, crop_id):
    pe_c = pe(Crop)
    pe_c_id = pe_c.by_id(G404=G404, id=crop_id)
    pe_cds = CDS.objects.filter(from_crop=crop_id)
    master_family = pe_c_id.family.name
    if pe_c_id.family.is_family_slave:
        master_family = pe_c_id.family.family_master.name
    context = {
        "family": master_family,
        "crop": pe_c_id,
        "sources": pe_cds,
    }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(skins=S, context=context)
    template = "strona/crop.html"
    return render(request, template, context_lazy)


# Widok szczegółowy danej rodziny, oraz "nibyrodzin" (patrz: owies)
def family(request, family_id):
    pe_f = pe(CropFamily)
    pe_f_id = pe_f.by_id(G404=G404, id=family_id)
    pe_f_id_sub = False
    if pe_f_id.is_family_slave:
        sub_id = pe_f_id.family_master.id
        pe_f_id_sub = pe_f.by_id(G404=G404, id=sub_id)
    family_slav_list = check_slaves(
        pe_f_id,
        pe_f_id_sub,
        pe_f_id.is_family_slave,
    )
    house = []
    for item in family_slav_list:
        pe_c_all = Crop.objects.filter(family=item.id)
        for crop_object in pe_c_all:
            house.append(crop_object)
    house = sorted(house, key=attrgetter('name'))
    context = {
        "family": family_slav_list[0],
        "house": house,
    }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(skins=S, context=context)
    template = "strona/family.html"
    return render(request, template, context_lazy)

# Widok pozwala userowi stworzyć zupełnie nowy plan.
@login_required
def my_plans(request):
    userdata = User.objects.get(
     id=request.user.id)
    pe_upl = pe(RotationPlan).allelements.filter(owner=userdata)
    user_limit_reached = False
    if len(list(pe_upl)) > 11:
        user_limit_reached = True

    if request.method == 'POST':
        form = RotationPlanForm(request.POST)
        if form.is_valid():
            form.save(user_id=userdata)
            return redirect('my_plans') # Przekierowuj później na stronę planu
    else:
        form = RotationPlanForm()
        context = {
         "form": form,
         "user_plans": pe_upl,
         "user_limit": user_limit_reached,
        }
        pl = PageLoad(P, L)
        context_lazy = pl.lazy_context(skins=S, context=context)
        template = "strona/my_plans.html"
        return render(request, template, context_lazy)


# Funkcja przekierowująca w zależnośni od tego,
# czy user dodał już chociaż jeden element do planu, czy nie
# i w razie czego wymusza jego dodanie.
# Sprawdza też, czy user jest właścicielem i jeśli nie jest wywala na główną.
@login_required
def plan_edit(request, plan_id):
    pe_rp = pe(RotationPlan)
    pe_rp_id = pe_rp.by_id(G404=G404, id=plan_id)
    if check_ownership(request, User, pe_rp_id):
        if RotationStep.objects.filter(from_plan=plan_id).exists():
            return redirect('plan', plan_id)
        else:
            if request.method == 'POST':
                form = FirstRotationStepForm(request.POST)
                if form.is_valid():
                    form.save(pe_rp_id)
                    return redirect('plan', plan_id) # Przekierowuj później na stronę planu
            else:
                form = FirstRotationStepForm()
                context = {
                 "form": form,
                }
                pl = PageLoad(P, L)
                context_lazy = pl.lazy_context(skins=S, context=context)
                template = "strona/first_step_create.html"
                return render(request, template, context_lazy)
    else:
       return redirect('home')




###### BRUDNOPIS ######
# userdata = User.objects.get(
# id=request.user.id)
# user_id = userdata.id
# flare(user_id)
# owner_id = pe_rp_id.owner.id
# flare(owner_id)
# if user_id == owner_id:
#    flare("True_af")
#    pass
# else:
#    flare("False_af")
#    pass
# return redirect('logger')
# Zrób jeśli user jest właścicielem, żeby mógł robić zmiany.
