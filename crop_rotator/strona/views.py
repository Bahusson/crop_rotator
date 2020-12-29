from django.shortcuts import (render, redirect, get_object_or_404 as G404)
from django.contrib.auth.models import User  # Zaimportuj uproszczony model usera.
from .models import (PageSkin as S,  PageNames as P, RegNames, AboutPageNames)
from rotator.models import (RotationPlan, RotationStep)
from crop_rotator.settings import LANGUAGES as L
from core.classes import (PageElement as pe, PageLoad)
from core.snippets import booleanate as bot, flare
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
        for i in i1[0]:
            cooldown_list.append(
             [i.family.cooldown_min, i.id, i.family, item.order, i])
            if i.family.is_mandatory_crop:
                fabacae.append(str(item.order) + "a")
        for i in i2[0]:
            cooldown_list.append(
             [i.family.cooldown_min, i.id, i.family, item.order, i])
            if i.family.is_mandatory_crop:
                fabacae.append(str(item.order) + "b")
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
    for item in cooldown_list:
        if item[0] > len_listed_pe_rs:
            error_len_crops.append(item[1])
            clw = Crop.objects.filter(id__in=error_len_crops)
    if not clw:
        for a, b in itertools.permutations(cooldown_list2, 2):  # permutacje
            if a[2] == b[2] and a[3] - b[3] < a[0] and a[3] - b[3] > 0:
                if a[3] > top_tier:
                    a[3] = a[3] - top_tier
                    if b[3] > top_tier:
                        b[3] = b[3] - top_tier
                err_tab_list.append(a[3])
                err_tab_list.append(b[3])
                err_crop_list.append(a + b)
                err_crop_list.append(b + a)
    fabs = []
    [fabs.append(x) for x in fabacae if x not in fabs]

    fabs_percent = float(len(fabs))/float(top_tier*2)
    fabs_rounded = round(fabs_percent, 2)
    fabs_error = False
    if fabs_rounded >= 0.25 and fabs_rounded <= 0.33:
    else:
        fabs_error = int(fabs_rounded * 100)
        fabs_error = str(fabs_error) + "%"
    res = []
    [res.append(x) for x in err_tab_list if x not in res]
    error_family_crops = {"e_crops": err_crop_list, "e_tabs": res,}
    context = {
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
