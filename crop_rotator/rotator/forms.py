from django import forms
from .models import RotationPlan, RotationStep
from core.classes import checkifnull as cn
from core.snippets import flare
import datetime


class RotationPlanForm(forms.ModelForm):
    title = forms.CharField(max_length=150, required=False)

    class Meta:
        model = RotationPlan
        fields = ("title", )

    def save(self, commit=True, **kwargs):
        plan = super(RotationPlanForm, self).save(commit=False)
        plan.title = self.cleaned_data["title"]
        if plan.owner is None:
            plan.owner = kwargs['user_id']
        if plan.pubdate is None:
            plan.pubdate = datetime.datetime.now()

        if commit:
            plan.save()
        return plan


class FirstRotationStepForm(forms.ModelForm):
    title = forms.CharField(max_length=150)
    class Meta:
        model = RotationStep
        fields = ("title", )

    def save(self, plan_id, commit=True):
        step = super(FirstRotationStepForm, self).save(commit=False)
        step.title = self.cleaned_data["title"]
        step.order = 1
        step.from_plan = plan_id

        if commit:
            step.save()
        return step


class NextRotationStepForm(forms.ModelForm):
    title = forms.CharField(max_length=150)
    class Meta:
        model = RotationStep
        fields = ("title", )

    def save(self, plan_id, step_order, commit=True):
        step = super(NextRotationStepForm, self).save(commit=False)
        step.title = self.cleaned_data["title"]
        step.order = int(step_order) + 1
        step.from_plan = plan_id

        if commit:
            step.save()
        return step



class UserPlanPublicationForm(forms.ModelForm):
    class Meta:
        model = RotationPlan
        fields = ("published",)

    def save(self, published, commit=True):
        plan = super(UserPlanPublicationForm, self).save(commit=False)
        flare(published)
        plan.published = published

        if commit:
            plan.save()
        return plan
