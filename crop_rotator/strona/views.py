from django.shortcuts import render, redirect, get_object_or_404 as G404
from django.contrib.auth.models import User
from .models import (
    PageSkin as S,
    PageNames as P,
    RegNames,
    AboutPageNames,
    RotatorEditorPageNames,
)
from django.views.decorators.cache import cache_page
from rotator.models import (
    RotationPlan,
    RotationStep,
    Crop,
    CropFamily,
    CropDataSource as CDS,
)
from crop_rotator.settings import LANGUAGES as L
from core.classes import (
    PageElement as pe,
    PageLoad,
    CropPlanner,
    DummyCropPlanner,
)
from core.snippets import (
    booleanate as bot,
    flare,
    level_off,
    list_appending_short,
    remove_repeating,
    repack,
    check_slaves,
    check_ownership,
    slice_list_3,
)
from django.contrib.auth.decorators import login_required
from rotator.forms import (
    RotationPlanForm,
    FirstRotationStepForm,
    NextRotationStepForm,
    UserPlanPublicationForm,
    StepMoveForm,
    StepEditionForm,
)
from rotator.models import Crop
from operator import attrgetter
from random import shuffle


# Widok strony domowej.
def home(request):
    pe_rp = pe(RotationPlan).allelements
    pe_rp_published = pe_rp.filter(published=True)
    pe_rp_shuffled = list(pe_rp_published)
    shuffle(pe_rp_shuffled)  # Losuje z widocznych na głównej.
    pe_rp_shuffled = pe_rp_shuffled[:4]
    
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


# Widok strony "O nawozach"
def fertilize(request):
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

#TODO: Z dwóch poniższych możesz zrobić widoki na klasie, bo są zbliżone.
# Widok planu po ewaluacji na życzenie.
#@cache_page(60)
def plan_evaluated(request, plan_id):
    pe_rp = pe(RotationPlan)
    pe_stp = pe(RotationStep)
    translatables = pe(RotatorEditorPageNames).baseattrs
    pe_rp_id = pe_rp.by_id(G404=G404, id=plan_id)
    user_editable = False
    if check_ownership(request, User, pe_rp_id):
        user_editable = True
    else:
        return redirect("lurk_plan", plan_id)
    form = NextRotationStepForm()
    form2 = StepMoveForm()
    context = {
        "user_editable": user_editable,  # Bramka dla zawartości widocznej tylko dla autora.
        "form": form,
        "form2": form2,
        "translatables": translatables,
    }
    cp = CropPlanner(pe_rp_id, RotationStep, Crop, plan_id=plan_id)
    plans_context = cp.basic_context(context=context)
    # Dodaj następny krok do planu
    if "next_step" in request.POST:
        form = NextRotationStepForm(request.POST)
        if form.is_valid():
            form.save(pe_rp_id, cp.top_tier)
            return redirect('plan', plan_id)
    # Usuń cały plan.
    if "delete_plan" in request.POST:
        pe_rp_id.delete()
        return redirect('my_plans')
    # Opublikuj plan.
    if "publish_plan" in request.POST:
        form = UserPlanPublicationForm(request.POST, instance=pe_rp_id)
        if form.is_valid():
            form.save(True)
            return redirect('plan', plan_id)
    # Wycofaj plan z pubilkacji.
    if "unpublish_plan" in request.POST:
        form = UserPlanPublicationForm(request.POST, instance=pe_rp_id)
        if form.is_valid():
            form.save(False)
            return redirect('plan', plan_id)
    if "receiver_step" in request.POST:
        sender_step_id = pe_stp.by_id(
         G404=G404, id=request.POST.get('sender_step'))
        try:
            receiver_step_id = pe_stp.by_id(
            G404=G404, id=request.POST.get('receiver_step'))
        except:
            return redirect('plan', plan_id)
        sender_step_order = sender_step_id.order
        form2 = StepMoveForm(request.POST, instance=sender_step_id)
        form3 = StepMoveForm(request.POST, instance=receiver_step_id)
        if form2.is_valid() and form3.is_valid():
            form2.save()
            form3.save(order=sender_step_order)
            return redirect('plan', plan_id)
    if "delete_step" in request.POST:
        last_step = pe_stp.by_id(G404=G404, id=request.POST.get('delete_step'))
        last_step.delete()
        return redirect('plan', plan_id)

    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(skins=S, context=plans_context)
    template = "strona/plan.html"
    return render(request, template, context_lazy)


# Widok pojedynczego płodozmianu dla Edytora - no_cache
def plan(request, plan_id):
    pe_rp = pe(RotationPlan)
    pe_stp = pe(RotationStep)
    translatables = pe(RotatorEditorPageNames).baseattrs
    pe_rp_id = pe_rp.by_id(G404=G404, id=plan_id)
    pe_rs = RotationStep.objects.filter(from_plan=plan_id)
    user_editable = False
    if check_ownership(request, User, pe_rp_id):
        user_editable = True
    else:
        return redirect("lurk_plan", plan_id)
    form = NextRotationStepForm()
    form2 = StepMoveForm()
    context = {
        "user_editable": user_editable,  # Bramka dla zawartości widocznej tylko dla autora.
        "form": form,
        "form2": form2,
        "translatables": translatables,
    }
    dcp = DummyCropPlanner(pe_rp_id, RotationStep, Crop, plan_id=plan_id)
    plans_context = dcp.basic_context(context=context)
    # Dodaj następny krok do planu
    if "next_step" in request.POST:
        form = NextRotationStepForm(request.POST)
        if form.is_valid():
            form.save(pe_rp_id, dcp.top_tier)
            return redirect(request.META.get('HTTP_REFERER'))
    # Usuń cały plan.
    if "delete_plan" in request.POST:
        pe_rp_id.delete()
        return redirect('my_plans')
    # Opublikuj plan.
    if "publish_plan" in request.POST:
        form = UserPlanPublicationForm(request.POST, instance=pe_rp_id)
        if form.is_valid():
            form.save(True)
            return redirect(request.META.get('HTTP_REFERER'))
    # Wycofaj plan z pubilkacji.
    if "unpublish_plan" in request.POST:
        form = UserPlanPublicationForm(request.POST, instance=pe_rp_id)
        if form.is_valid():
            form.save(False)
            return redirect(request.META.get('HTTP_REFERER'))
    if "receiver_step" in request.POST:
        sender_step_id = pe_stp.by_id(
         G404=G404, id=request.POST.get('sender_step'))
        get_receiver = request.POST.get('receiver_step')
        try:
            receiver_step_id = pe_stp.by_id(
            G404=G404, id=request.POST.get('receiver_step'))
        except:
            return redirect(request.META.get('HTTP_REFERER'))
        sender_step_order = sender_step_id.order
        form2 = StepMoveForm(request.POST, instance=sender_step_id)
        form3 = StepMoveForm(request.POST, instance=receiver_step_id)
        if form2.is_valid() and form3.is_valid():
            form2.save()
            form3.save(order=sender_step_order)
            return redirect(request.META.get('HTTP_REFERER'))
    if "delete_step" in request.POST:
        last_step = pe_stp.by_id(G404=G404, id=request.POST.get('delete_step'))
        last_step.delete()
        return redirect(request.META.get('HTTP_REFERER'))

    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(skins=S, context=plans_context)
    template = "strona/plan.html"
    return render(request, template, context_lazy)


# Widok pojedynczego płodozmianu dla lurkera - longcache 24h - Popraw czas w produkcji
@cache_page(60 * 15)
def lurk_plan(request, plan_id):
    pe_rp = pe(RotationPlan)
    pe_rp_id = pe_rp.by_id(G404=G404, id=plan_id)
    translatables = pe(RotatorEditorPageNames).baseattrs
    user_editable = False
    context = {
        "user_editable": user_editable,  # Bramka dla zawartości widocznej tylko dla autora.
        "translatables": translatables,
    }
    dcp = DummyCropPlanner(pe_rp_id, RotationStep, Crop, plan_id=plan_id)
    plans_context = dcp.basic_context(context=context)
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
    translatables = pe(RotatorEditorPageNames).baseattrs
    if pe_c_id.family.is_family_slave:
        master_family = pe_c_id.family.family_master.name
    context = {
        "family": master_family,
        "crop": pe_c_id,
        "sources": pe_cds,
        "translatables": translatables,
    }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(skins=S, context=context)
    template = "strona/crop.html"
    return render(request, template, context_lazy)


# Spis wszystkich rodzin, bez "nibyrodzin" (typu owies u wiechlinowatych).
def all_plant_families(request):
    pe_f = pe(CropFamily).allelements
    pe_f_master_list = []
    for item in pe_f:
        if item.is_family_slave:
            pass
        else:
            pe_f_master_list.append(item)
    sl3 = slice_list_3(pe_f_master_list)
    context = {
        "families": pe_f_master_list,
        "ml1": sl3[0],
        "ml2": sl3[1],
    }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(skins=S, context=context)
    template = "strona/all_plant_families.html"
    return render(request, template, context_lazy)


# Widok szczegółowy danej rodziny, oraz "nibyrodzin" (patrz: owies)
def family(request, family_id):
    pe_f = pe(CropFamily)
    pe_f_id = pe_f.by_id(G404=G404, id=family_id)
    pe_f_id_sub = False
    translatables = pe(RotatorEditorPageNames).baseattrs
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
    sl3 = slice_list_3(house)
    context = {
        "family": family_slav_list[0],
        "house": house,
        "ml1": sl3[0],
        "ml2": sl3[1],
        "translatables": translatables,
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
    translatables = pe(RotatorEditorPageNames).baseattrs
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
         "translatables": translatables,

        }
        pl = PageLoad(P, L)
        context_lazy = pl.lazy_context(skins=S, context=context)
        template = "strona/my_plans.html"
        return render(request, template, context_lazy)


# Funkcja przekierowująca w zależnośni od tego,
# czy user dodał już chociaż jeden element do planu, czy nie
# i w razie czego wymusza jego dodanie.
@login_required
def plan_edit(request, plan_id):
    pe_rp = pe(RotationPlan)
    pe_rp_id = pe_rp.by_id(G404=G404, id=plan_id)
    translatables = pe(RotatorEditorPageNames).baseattrs
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
                 "translatables": translatables,
                }
                pl = PageLoad(P, L)
                context_lazy = pl.lazy_context(skins=S, context=context)
                template = "strona/first_step_create.html"
                return render(request, template, context_lazy)
    else:
       return redirect('home')


# Widok edycji pojedynczego kroku w planie zmianowania.
@login_required
def step(request, step_id):
    pe_stp = pe(RotationStep)
    pe_stp_id = pe_stp.by_id(G404=G404, id=step_id)
    plan_id = pe_stp_id.from_plan.id
    translatables = pe(RotatorEditorPageNames).baseattrs
    if check_ownership(request, User, pe_stp_id.from_plan):
        if "save_step_changes" in request.POST:
            form = StepEditionForm(request.POST, instance=pe_stp_id)
            if form.is_valid():
                form.save()
                return redirect('plan', plan_id)
        form = StepEditionForm(instance=pe_stp_id)
        context = {
         "form": form,
         "step": pe_stp_id,
         "translatables": translatables,
        }
        pl = PageLoad(P, L)
        context_lazy = pl.lazy_context(skins=S, context=context)
        template = "strona/step.html"
        return render(request, template, context_lazy)
    else:
        return redirect('home')
