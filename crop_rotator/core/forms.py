from django import forms
from .models import RotatorAdminPanel
from .snippets import flare


class RotatorAdminPanelForm(forms.ModelForm):

    class Meta:
        model = RotatorAdminPanel
        fields = (
         "max_steps", "max_user_plans", "lurk_plan_cooldown",
          "evaluated_plan_cooldown",
         )

    def save(self, commit=True):
        panel = super(RotatorAdminPanelForm, self).save(commit=False)
        panel.max_steps = self.cleaned_data["max_steps"]
        panel.max_user_plans = self.cleaned_data["max_user_plans"]
        panel.lurk_plan_cooldown = self.cleaned_data["lurk_plan_cooldown"]
        panel.evaluated_plan_cooldown = self.cleaned_data["evaluated_plan_cooldown"]


        if commit:
            panel.save()
        return panel
