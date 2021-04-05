from django.shortcuts import render, redirect, get_object_or_404 as G404
from django.contrib.auth.models import User
from strona.models import (
    PageSkin as S,
    PageNames as P,
    RegNames,
    AboutPageNames,
    RotatorEditorPageNames,
)
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rekruter.models import (
    RotationPlan,
    RotationStep,
)
from rotator.models import (
    Crop,
)
from crop_rotator.settings import LANGUAGES as L
from core.classes import (
    PageElement as pe,
    PageLoad,
    CropPlanner,
    DummyCropPlanner,
    edit_delay_sec,
    lurk_delay_min,
)
from core.snippets import (
    flare,
    level_off,
    list_appending_short,
    remove_repeating,
    repack,
    check_ownership,
    slice_list_3,
    summarize_plans,
)
from core.models import RotatorAdminPanel
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
from django.views import View


# Widok wszystkich płodozmianów - dodać wyszukiwarkę?
def allplans(request):
    pe_rp_published = RotationPlan.objects.filter(published=True)
    plans_list = summarize_plans(pe_rp_published, RotationStep)
    context = {
        "rotation_plans": plans_list,
    }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(skins=S, context=context)
    template = "strona/allplans.html"
    return render(request, template, context_lazy)


# Widok źródłowy dla planów do edycji i ewaluacji.
class Plan(View):
    user_editable = True
    VarCropPlanner = DummyCropPlanner

    def dispatch(self, request, plan_id, *args, **kwargs):
        admin_max_steps = pe(RotatorAdminPanel).baseattrs.max_steps -1
        pe_rp = pe(RotationPlan)
        self.pe_stp = pe(RotationStep)
        translatables = pe(RotatorEditorPageNames).baseattrs
        self.plan_id=plan_id
        self.pe_rp_id = pe_rp.by_id(G404=G404, id=self.plan_id)
        if self.user_editable:
            if not check_ownership(request, User, self.pe_rp_id):
                return ("lurk_plan", self.plan_id)
        form = NextRotationStepForm()
        form2 = StepMoveForm()
        form3 = RotationPlanForm()
        context = {
            "user_editable": self.user_editable,  # Bramka dla zawartości widocznej tylko dla autora.
            "form": form,
            "form2": form2,
            "form3": form3,
            "admin_max_steps": admin_max_steps,
            "translatables": translatables,
            }
        self.cp = self.VarCropPlanner(self.pe_rp_id, RotationStep, Crop, plan_id=self.plan_id)
        self.plans_context = self.cp.basic_context(context=context)
        return super(Plan, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Dodaj następny krok do planu
        if "next_step" in request.POST:
            form = NextRotationStepForm(request.POST)
            if form.is_valid():
                form.save(self.pe_rp_id, self.cp.top_tier)
                return redirect('plan', self.plan_id)
        # Usuń cały plan.
        if "delete_plan" in request.POST:
            self.pe_rp_id.delete()
            return redirect('my_plans', )
        # Opublikuj plan.
        if "publish_plan" in request.POST:
            form = UserPlanPublicationForm(request.POST, instance=self.pe_rp_id)
            if form.is_valid():
                form.save(True)
                return redirect('plan', self.plan_id)
        # Wycofaj plan z pubilkacji.
        if "unpublish_plan" in request.POST:
            form = UserPlanPublicationForm(request.POST, instance=self.pe_rp_id)
            if form.is_valid():
                form.save(False)
                return redirect('plan', self.plan_id)
        # zamień kroki miejscami
        if "receiver_step" in request.POST:
            sender_step_id = self.pe_stp.by_id(
             G404=G404, id=request.POST.get('sender_step'))
            try:
                receiver_step_id = self.pe_stp.by_id(
                G404=G404, id=request.POST.get('receiver_step'))
            except:
                return redirect('plan', self.plan_id)
            sender_step_order = sender_step_id.order
            form1 = StepMoveForm(request.POST, instance=sender_step_id)
            form2 = StepMoveForm(request.POST, instance=receiver_step_id)
            if form1.is_valid() and form2.is_valid():
                form1.save()
                form2.save(order=sender_step_order)
                return redirect('plan', self.plan_id)
        # Usuń krok
        if "delete_step" in request.POST:
            last_step = self.pe_stp.by_id(G404=G404, id=request.POST.get('delete_step'))
            last_step.delete()
            return redirect('plan', self.plan_id)
        # Edytuj tytuł planu.
        if "edit_plan_title" in request.POST:
            form = RotationPlanForm(request.POST, instance=self.pe_rp_id)
            if form.is_valid():
                form.save()
                return redirect('plan', self.plan_id)

    def get(self, request, *args, **kwargs):
        pl = PageLoad(P, L)
        context_lazy = pl.lazy_context(skins=S, context=self.plans_context)
        template = "strona/plan.html"
        return render(request, template, context_lazy)


# Subklasowany widok powyżej używany tylko do aktu ewaluacji planu. Ma wbudowane cache.
@method_decorator(cache_page(edit_delay_sec), name='dispatch')
class PlanEvaluated(Plan):
    VarCropPlanner = CropPlanner


# Subklasowany widok pojedynczego płodozmianu dla lurkera
@method_decorator(cache_page(60 * lurk_delay_min), name='dispatch')
class LurkPlan(Plan):
    user_editable = False


# Widok pozwala userowi stworzyć zupełnie nowy plan.
@login_required
def my_plans(request):
    admin_max_plans = pe(RotatorAdminPanel).baseattrs.max_user_plans
    userdata = User.objects.get(
     id=request.user.id)

    try:
        pe_upl = pe(RotationPlan).allelements.filter(owner=userdata)
    except:
        pe_upl = []
    plans_list = summarize_plans(pe_upl, RotationStep)
    translatables = pe(RotatorEditorPageNames).baseattrs
    user_limit_reached = False
    if len(list(pe_upl)) > admin_max_plans-1:
        user_limit_reached = True

    if request.method == 'POST':
        form = RotationPlanForm(request.POST)
        if form.is_valid():
            form.save(user_id=userdata)
            return redirect('my_plans') # Przekierowuj później na stronę planu
    else:
        form = RotationPlanForm()
        sl3 = slice_list_3(plans_list)
        context = {
         "form": form,
         "user_plans": plans_list,
         "ml1": sl3[0],
         "ml2": sl3[1],
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

def removedict(pe_stp_id, remove_key, element_to_remove):
    removedict = {
        "early": pe_stp_id.early_crop.remove(element_to_remove),
        "middle": pe_stp_id.middle_crop.remove(element_to_remove),
        "late": pe_stp_id.late_crop.remove(element_to_remove)
        }
    return removedict[remove_key]

# Widok edycji pojedynczego kroku w planie zmianowania.
@login_required
def step(request, step_id):
    croplist = Crop.objects.all()
    pe_stp = pe(RotationStep)
    pe_stp_id = pe_stp.by_id(G404=G404, id=step_id)
    plan_id = pe_stp_id.from_plan.id
    translatables = pe(RotatorEditorPageNames).baseattrs
    if check_ownership(request, User, pe_stp_id.from_plan):
        if "save_step_changes" in request.POST:
            form = StepEditionForm(request.POST, instance=pe_stp_id)
            if form.is_valid():
                form.save()
                return redirect('step', step_id)
        # Usuwa po jednym elemencie z każdego kroku.
        # Nie lubię tego kodu, ale nie mam na razie pomysłu na inny.
        if "remove_element_button" in request.POST:
            element_to_remove = request.POST.get('remove_element')
            remove_key = request.POST.get('remove_key')
            if request.POST.get('remove_key') == "early":
                pe_stp_id.early_crop.remove(element_to_remove)
            elif request.POST.get('remove_key') == "middle":
                pe_stp_id.middle_crop.remove(element_to_remove)
            elif request.POST.get('remove_key') == "late":
                pe_stp_id.late_crop.remove(element_to_remove)
            return redirect('step', step_id)
        if "add_element_button" in request.POST:
        # Dodaje po jednym elemencie do każdego kroku.
            element_to_add = request.POST.get('add_element')
            add_key = request.POST.get('remove_key')
            if request.POST.get('add_key') == "early":
                try:
                    pe_stp_id.early_crop.add(element_to_add)
                except :
                    pass
            elif request.POST.get('add_key') == "middle":
                try:
                    pe_stp_id.middle_crop.add(element_to_add)
                except:
                    pass
            elif request.POST.get('add_key') == "late":
                try:
                    pe_stp_id.late_crop.add(element_to_add)
                except:
                    pass
            return redirect('step', step_id)


        form = StepEditionForm(instance=pe_stp_id)
        context = {
         "croplist": croplist,
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
