from django import forms
from rekruter.models import RotationPlan, RotationStep, RotationSubStep
from core.snippets import flare
import datetime


class RotationPlanForm(forms.ModelForm):
    title = forms.CharField(max_length=150, required=True)

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
        plan.published = published

        if commit:
            plan.save()
        return plan


class StepEditionForm(forms.ModelForm):
    class Meta:
        model = RotationStep
        fields = (
         "title", "descr"
         )

    def save(self, commit=True):
        step = super(StepEditionForm, self).save(commit=False)
        step.title = self.cleaned_data["title"]
        step.descr = self.cleaned_data["descr"]

        if commit:
            step.save()
        return step


# Służy do zamiany dowolnych dwóch kroków miejscami (zamienia im indeksowanie)
class StepMoveForm(forms.ModelForm):
    receiver_step_order = forms.CharField(
     widget=forms.HiddenInput(), required=False)
    sender_step = forms.CharField(widget=forms.HiddenInput(), required=False)
    receiver_step = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = RotationStep
        fields = ("order",)

    def save(self, commit=True, **kwargs):
        step = super(StepMoveForm, self).save(commit=False)
        if "order" in kwargs:
            step.order = int(kwargs['order'])
        else:
            step.order = int(self.cleaned_data["receiver_step_order"])

        if commit:
            step.save()
        return step
