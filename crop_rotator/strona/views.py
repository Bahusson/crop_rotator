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
from core.classes import PageElement as pe, PageLoad
from core.snippets import (
    booleanate as bot,
    flare,
    level_off,
    list_appending_short,
    remove_repeating,
    repack,
    check_slaves,
)
from django.contrib.auth.decorators import login_required
from rotator.forms import (
    RotationPlanForm,
    FirstRotationStepForm,
    NextRotationStepForm,
    UserPlanPublicationForm
)
from rotator.models import Crop
import itertools
import copy
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
    user_editable = False
    pe_rp = pe(RotationPlan)
    pe_rp_id = pe_rp.by_id(G404=G404, id=plan_id)
    userdata = User.objects.get(
    id=request.user.id)
    user_id = userdata.id
    owner_id = pe_rp_id.owner.id
    if user_id == owner_id:
        user_editable = True
    pe_rs = RotationStep.objects.filter(from_plan=plan_id)
    listed_pe_rs = list(pe_rs)
    len_listed_pe_rs = len(listed_pe_rs)
    cooldown_list = []
    fabacae = []
    top_tier_list = []
    for item in listed_pe_rs:
        i1 = (list(item.early_crop.all()), item.order)
        i2 = (list(item.late_crop.all()), item.order)
        i3 = item.order
        top_tier_list.append(i3)
        vars = [cooldown_list, item, fabacae]
        list_appending_short(i1, "a", vars)
        list_appending_short(i2, "b", vars)
    cooldown_list.sort()
    top_tier_list.sort()
    clw = False
    error_len_crops = []
    cooldown_list1 = copy.deepcopy(cooldown_list)  # kopiowanie listy
    top_tier = top_tier_list[-1]
    for item in cooldown_list1:
        item[3][0] += top_tier
    cooldown_list2 = cooldown_list + cooldown_list1
    err_tab_list = []
    err_crop_list = []
    crop_interaction_list = []
    family_interaction_list = []
    crop_interaction_list_f = []
    family_interaction_list_f = []
    for item in cooldown_list:
        if item[0] > len_listed_pe_rs:
            error_len_crops.append(item[1])
            clw = Crop.objects.filter(id__in=error_len_crops)
    if not clw:
        for a, b in itertools.permutations(cooldown_list2, 2):  # permutacje
            if a[2] == b[2] and a[3][0] - b[3][0] < a[0] and a[3][0] - b[3][0] > 0:
                level_off(top_tier, a, b)
                err_tab_list.append(a[3][0])
                err_tab_list.append(b[3][0])
                err_crop_list.append(a + b)
                err_crop_list.append(b + a)
            if a[4].crop_relationships.filter(about_crop__id=b[4].id).exists():
                for i in a[4].crop_relationships.filter(about_crop__id=b[4].id):
                    if (
                        a[3][1] == b[3][1] - i.start_int
                        or a[3][1] == b[3][1] - i.end_int
                    ):
                        level_off(top_tier, a, b)
                        crop_interaction_list.append(a + b + [i.is_positive])
            if a[4].crop_relationships.filter(about_family__id=b[2].id).exists():
                for i in a[4].crop_relationships.filter(about_family__id=b[2].id):
                    if (
                        a[3][1] == b[3][1] - i.start_int
                        or a[3][1] == b[3][1] - i.end_int
                    ):
                        level_off(top_tier, a, b)
                        family_interaction_list.append(a + b + [i.is_positive])
            if a[4].family.family_relationships.filter(about_crop__id=b[4].id).exists():
                for i in a[4].family.family_relationships.filter(
                    about_crop__id=b[4].id
                ):
                    if (
                        a[3][1] == b[3][1] - i.start_int
                        or a[3][1] == b[3][1] - i.end_int
                    ):
                        level_off(top_tier, a, b)
                        crop_interaction_list_f.append(a + b + [i.is_positive])
            if (
                a[4]
                .family.family_relationships.filter(about_family__id=b[2].id)
                .exists()
            ):
                for i in a[4].family.family_relationships.filter(
                    about_family__id=b[2].id
                ):
                    if (
                        a[3][1] == b[3][1] - i.start_int
                        or a[3][1] == b[3][1] - i.end_int
                    ):
                        level_off(top_tier, a, b)
                        family_interaction_list_f.append(a + b + [i.is_positive])
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
    fabs = []
    tabs = []
    interactions = []
    interactions_f = []
    f_interactions = []
    f_interactions_f = []
    remove_repeating(fabs, fabacae)
    remove_repeating(tabs, err_tab_list)
    remove_repeating(interactions, crop_interaction_list)
    remove_repeating(interactions_f, family_interaction_list)
    remove_repeating(f_interactions, crop_interaction_list_f)
    remove_repeating(f_interactions_f, family_interaction_list_f)
    fabs_percent = float(len(fabs)) / float(top_tier * 2)
    fabs_rounded = round(fabs_percent, 2)
    fabs_error = False
    if fabs_rounded >= 0.25 and fabs_rounded <= 0.33:
        pass
    else:
        fabs_error = int(fabs_rounded * 100)
        fabs_error = str(fabs_error) + "%"
    error_family_crops = {
        "e_crops": err_crop_list,
        "e_tabs": tabs,
    }
    form = NextRotationStepForm()
    context = {
        "user_editable": user_editable,  # Bramka dla zawartości widocznej tylko dla autora.
        "form": form,
        "interactions": interactions,
        "interactions_f": interactions_f,
        "f_interactions": f_interactions,
        "f_interactions_f": f_interactions_f,
        "f_error": fabs_error,
        "efcs": error_family_crops,
        "cr_len_warning": clw,
        "plan": pe_rp_id,
        "steps": pe_rs,
    }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(skins=S, context=context)
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
    userdata = User.objects.get(
    id=request.user.id)
    user_id = userdata.id
    owner_id = pe_rp_id.owner.id
    if user_id == owner_id:
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
