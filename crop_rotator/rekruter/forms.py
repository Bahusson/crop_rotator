from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ExtendedCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(ExtendedCreationForm, self).save(commit=False)
        user.username = self.cleaned_data["username"]

        if commit:
            user.save()
        return user
