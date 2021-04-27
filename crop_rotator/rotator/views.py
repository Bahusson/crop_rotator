from django.shortcuts import render, redirect, get_object_or_404 as G404
from django.contrib.auth.models import User
from strona.models import (
    PageSkin as S,
    PageNames as P,
    RotatorEditorPageNames,
)
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rekruter.models import (
    RotationPlan,
    RotationStep,
    RotationSubStep,
)
from rotator.models import (
    Crop,
    MixCrop,
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
    check_ownership,
    slice_list_3,
    summarize_plans,
    compare_csv_lists,
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
from django.views import View


# Widok wszystkich płodozmianów - dodać wyszukiwarkę?
def allplans(request):
    pe_rp_published = RotationPlan.objects.filter(published=True)
    plans_list = summarize_plans(pe_rp_published, RotationSubStep)
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
    eval_button_on = True
    VarCropPlanner = DummyCropPlanner

    def dispatch(self, request, plan_id, *args, **kwargs):
        admin_max_steps = pe(RotatorAdminPanel).baseattrs.max_steps - 1
        pe_rp = pe(RotationPlan)
        self.pe_stp = pe(RotationStep)
        translatables = pe(RotatorEditorPageNames).baseattrs
        self.plan_id = plan_id
        self.pe_rp_id = pe_rp.by_id(G404=G404, id=self.plan_id)
        if self.user_editable:
            if not check_ownership(request, User, self.pe_rp_id):
                return ("lurk_plan", self.plan_id)
        form = NextRotationStepForm()
        form2 = StepMoveForm()
        form3 = RotationPlanForm()
        context = {
            "user_editable": self.user_editable,
            "form": form,
            "form2": form2,
            "form3": form3,
            "admin_max_steps": admin_max_steps,
            "translatables": translatables,
            "eval_button_on": self.eval_button_on,
            }
        self.cp = self.VarCropPlanner(
         self.pe_rp_id, RotationStep, Crop, RotationSubStep,
         plan_id=self.plan_id)
        self.plans_context = self.cp.basic_context(context=context)
        return super(Plan, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Dodaj następny krok do planu
        if "next_step" in request.POST:
            form = NextRotationStepForm(request.POST)
            if form.is_valid():
                form.save(self.pe_rp_id, self.cp.top_tier)
                newsteps = RotationStep.objects.filter(
                 from_plan=self.pe_rp_id)
                newstep_list = []
                for newstep in newsteps:
                    newstep_list.append(newstep.id)
                newstep_id = max(newstep_list)
                return redirect('step', newstep_id)
        # Usuń cały plan. -# TODO: Można przenieść do managera, w update
        # bo mamy w tej funkcji max złożoność cyklomatyczną.
        if "delete_plan" in request.POST:
            self.pe_rp_id.delete()
            return redirect('my_plans', )
        # Opublikuj plan. Też można przenieść do managera.
        if "publish_plan" in request.POST:
            form = UserPlanPublicationForm(
             request.POST, instance=self.pe_rp_id)
            if form.is_valid():
                form.save(True)
                return redirect('plan', self.plan_id)
        # Wycofaj plan z pubilkacji. Też można dać do managera.
        if "unpublish_plan" in request.POST:
            form = UserPlanPublicationForm(
             request.POST, instance=self.pe_rp_id)
            if form.is_valid():
                form.save(False)
                return redirect('plan', self.plan_id)
        # zamień kroki miejscami
        if "receiver_step" in request.POST:
            sender_step_id = self.pe_stp.by_id(
             G404=G404, id=request.POST.get('sender_step'))
            receiver_step_id = self.pe_stp.by_id(
             G404=G404, id=request.POST.get('receiver_step'))
            sender_step_order = sender_step_id.order
            form1 = StepMoveForm(request.POST, instance=sender_step_id)
            form2 = StepMoveForm(request.POST, instance=receiver_step_id)
            if form1.is_valid() and form2.is_valid():
                form1.save()
                form2.save(order=sender_step_order)
                return redirect('plan', self.plan_id)
        # Usuń krok
        if "delete_step" in request.POST:
            last_step = self.pe_stp.by_id(
             G404=G404, id=request.POST.get('delete_step'))
            last_step.delete()
            return redirect('plan', self.plan_id)
        # Edytuj tytuł planu. Do mangera, albo na inny widok.
        # Taki np. robią button typu "ustawienia" z obrazkiem klucza lub coga.
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


# Subklasowany widok powyżej używany tylko do aktu ewaluacji planu.
@method_decorator(cache_page(edit_delay_sec), name='dispatch')
class PlanEvaluated(Plan):
    VarCropPlanner = CropPlanner
    eval_button_on = False


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
    plans_list = summarize_plans(pe_upl, RotationSubStep)
    translatables = pe(RotatorEditorPageNames).baseattrs
    user_limit_reached = False
    if len(list(pe_upl)) > admin_max_plans-1:
        user_limit_reached = True

    if request.method == 'POST':
        form = RotationPlanForm(request.POST)
        if form.is_valid():
            form.save(user_id=userdata)
            return redirect('my_plans')
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
                    return redirect('plan', plan_id)
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


def changed_element(request):
    element_to_change = request.POST.get('inter_element')
    change_key = request.POST.get('inter_key')
    rss_object = pe(RotationSubStep).by_id(G404=G404, id=change_key)
    return (rss_object, element_to_change)


# Widok edycji pojedynczego kroku w planie zmianowania.
@login_required
def step(request, step_id):
    croplist = Crop.objects.all()
    pe_stp = pe(RotationStep)
    pe_stp_id = pe_stp.by_id(G404=G404, id=step_id)
    translatables = pe(RotatorEditorPageNames).baseattrs
    rss_objects = RotationSubStep.objects.filter(from_step=pe_stp_id)
    if check_ownership(request, User, pe_stp_id.from_plan):
        if "save_step_changes" in request.POST:
            form = StepEditionForm(request.POST, instance=pe_stp_id)
            if form.is_valid():
                form.save()
                return redirect('step', step_id)
        if "remove_element_button" in request.POST:
            rss_object = changed_element(request)
            rss_object[0].crop_substep.remove(rss_object[1])
            compare_csv_lists(MixCrop, rss_object[0].crop_substep)
            return redirect('step', step_id)
        if "add_element_button" in request.POST:
            try:
                rss_object = changed_element(request)
            except ValueError:
                return redirect('step', step_id)
            rss_object[0].crop_substep.add(rss_object[1])
            compare_csv_lists(MixCrop, rss_object[0].crop_substep)
            return redirect('step', step_id)
        if "add_substep_button" in request.POST:
            local_order = request.POST.get('inter_key')
            for rss_object in rss_objects:
                if rss_object.order == local_order:
                    return redirect("step", step_id)
            ss = RotationSubStep.create(local_order, pe_stp_id)
            ss.save()
            return redirect('step', step_id)
        if "remove_substep_button" in request.POST:
            substep_id = request.POST.get('inter_key')
            substep_to_delete = pe(
             RotationSubStep).by_id(G404=G404, id=substep_id)
            substep_to_delete.delete()
            return redirect('step', step_id)
        form = StepEditionForm(instance=pe_stp_id)
        context = {
         "croplist": croplist,
         "form": form,
         "step": pe_stp_id,
         "substeps": rss_objects,
         "translatables": translatables,
         "buttons": [1, 2, 3],
        }
        pl = PageLoad(P, L)
        context_lazy = pl.lazy_context(skins=S, context=context)
        template = "strona/step.html"
        return render(request, template, context_lazy)
    else:
        return redirect('home')
