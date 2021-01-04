from django.shortcuts import (render, redirect, get_object_or_404 as G404)
from django.contrib.auth.models import User  # Zaimportuj uproszczony model usera.
from .models import (PageSkin as S,  PageNames as P, RegNames, AboutPageNames)
from rotator.models import (RotationPlan, RotationStep)
from crop_rotator.settings import LANGUAGES as L
from core.classes import (PageElement as pe, PageLoad)
from core.snippets import (booleanate as bot, flare, level_off,
 list_appending_short, remove_repeating, repack)
from rotator.models import Crop
import itertools
import copy


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
    # Linijka userdata z brudnopisu wrzuć tutaj późnej.
    pe_rs = RotationStep.objects.filter(from_plan=plan_id)
    listed_pe_rs = list(pe_rs)
    len_listed_pe_rs = len(listed_pe_rs)
    lpr = listed_pe_rs[0]
    cooldown_list = []
    fabacae = []
    top_tier_list = []
    for item in listed_pe_rs:
        i1 = (list(item.early_crop.all()), item.order)
        i2 = (list(item.late_crop.all()), item.order)
        i3 = item.order
        top_tier_list.append(i3)
        vars =[cooldown_list, item, fabacae]
        list_appending_short(i1, "a", vars)
        list_appending_short(i2, "b", vars)
    cooldown_list.sort()
    top_tier_list.sort()
    clw = False
    error_len_crops = []
    cooldown_list1 = copy.deepcopy(cooldown_list)  # kopiowanie listy
    top_tier = top_tier_list[-1]
    for item in cooldown_list1:
        item[3] += top_tier
    cooldown_list2 = cooldown_list + cooldown_list1
    err_tab_list = []
    err_crop_list = []
    allelopatic_list = []
    synergic_list = []
    allelopatic_list_family = []
    synergic_list_family = []
    crop_interaction_list = []
    for item in cooldown_list:
        if item[0] > len_listed_pe_rs:
            error_len_crops.append(item[1])
            clw = Crop.objects.filter(id__in=error_len_crops)
    if not clw:
        for a, b in itertools.permutations(cooldown_list2, 2):  # permutacje
            if a[2] == b[2] and a[3] - b[3] < a[0] and a[3] - b[3] > 0:
                level_off(top_tier, a, b)
                err_tab_list.append(a[3])
                err_tab_list.append(b[3])
                err_crop_list.append(a + b)
                err_crop_list.append(b + a)
            if a[4].crop_relationships.filter(about_crop__id=b[4].id).exists():
                for i in a[4].crop_relationships.filter(about_crop__id=b[4].id):
                    if a[3] == b[3]-i.start_int or a[3] == b[3]-i.end_int:
                        level_off(top_tier, a, b)
                        crop_interaction_list.append(a + b + [i.is_positive])

        #    if a[4].crop_relationships.filter(about_family__id=b[2].id).exists():

            if a[4].allelopatic_to_family.filter(pk=b[2].id).exists():
                if a[3] == b[3] or a[3] == b[3]-1:
                    level_off(top_tier, a, b)
                    allelopatic_list_family.append(a + b)
            if a[4].synergic_to_family.filter(pk=b[2].id).exists() and a[3] == b[3]:
                level_off(top_tier, a, b)
                synergic_list_family.append(a + b)

    interactions = [k for k, g in itertools.groupby(sorted(crop_interaction_list))]
    allels_family = []
    synergies_family =[]
    fabs = []
    tabs = []
    remove_repeating(allels_family, allelopatic_list_family)
    remove_repeating(synergies_family, synergic_list_family)
    remove_repeating(fabs, fabacae)
    remove_repeating(tabs, err_tab_list)
    allels_family = repack(allels_family)
    synergies_family = repack(synergies_family)
    fabs_percent = float(len(fabs))/float(top_tier*2)
    fabs_rounded = round(fabs_percent, 2)
    fabs_error = False
    if fabs_rounded >= 0.25 and fabs_rounded <= 0.33:
        pass
    else:
        fabs_error = int(fabs_rounded * 100)
        fabs_error = str(fabs_error) + "%"
    error_family_crops = {"e_crops": err_crop_list, "e_tabs": tabs,}
    context = {
     'interactions': interactions,
     'allelopatic_f': allels_family,
     'synergic_f': synergies_family,
     'f_error': fabs_error,
     'efcs': error_family_crops,
     'cr_len_warning': clw,
     'plan': pe_rp_id,
     'steps': pe_rs,
     }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/plan.html'
    return render(request, template, context_lazy)

###### BRUDNOPIS ######
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
