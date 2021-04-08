from django import forms
from .models import RotatorAdminPanel
from rotator.models import CropsInteraction, FamilyInteraction
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


class ChangeElementCropsInteractionsForm(forms.ModelForm):

    class Meta:
        model = CropsInteraction
        fields = (
         "title", "is_positive", "about_crop", "about_family", "about_tag",
         "type_of_interaction", "season_of_interaction",
        )

    def save(self, cropname, is_pos, about_c, about_f, about_t, type_of_i, season_of_i, commit=True):
        element = super(ChangeElementCropsInteractionsForm, self).save(commit=False)
        element.title = cropname + " " + str(is_pos) + " " + about_c + " (" + type_of_i + ")(" + season_of_i + ")"
        element.is_positive = is_pos
        element.about_crop = about_c
        element.about_family = about_f
        element.about_tag = about_t
        element.type_of_interaction = type_of_i
        element.season_of_interaction = season_of_i

        if commit:
            element.save()
        return element



class ChangeElementFamilyInteractionsForm(ChangeElementCropsInteractionsForm):

    class Meta:
        model = FamilyInteraction
        fields = (
         "title", "is_positive", "about_crop", "about_family", "about_tag",
         "type_of_interaction", "season_of_interaction",
        )
