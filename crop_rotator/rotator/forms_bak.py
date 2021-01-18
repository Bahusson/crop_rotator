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

        if commit:
            plan.save()
        return plan


class FirstRotationStepForm(forms.ModelForm):
    title = forms.CharField(max_length=150)

    class Meta:
        model = RotationStep
        fields = ("title", "from_plan", )

    def save(self, user_id, commit=True):
        if self.from_plan is None:
            self.model = RotationPlan.objects.create(
             title=self.cleaned_data["title"],
             owner=user_id,
             pubdate = datetime.datetime.now(),)
        step = super(PartyDividerForm, self).save(commit=False)
        step.title = self.cleaned_data["title"] + " step"
        step.order = 1

        if commit:
            step.save()
        return step
