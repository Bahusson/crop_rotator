from django import forms
from .models import RotationPlan, RotationStep
from core.classes import checkifnull as cn
#  from core.snippets import flare
import datetime





class RotationPlanForm(forms.ModelForm):
    title = forms.CharField(max_length=150, required=False)

    class Meta:
        model = RotationPlan
        fields = ("title", )

    def save(self, user_id, commit=True):
        plan = super(RotationPlanForm, self).save(commit=False)
        plan.title = self.cleaned_data["title"]
        if plan.owner is None:
            plan.owner = user_id
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
        step = super(PartyDividerForm, self).save(commit=False)
        step.title = self.cleaned_data["title"]
        step.order = 1
        step.from_plan = plan_id

        if commit:
            step.save()
        return step
