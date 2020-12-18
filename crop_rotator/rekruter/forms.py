from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from core.snippets import gen_login


class ExtendedCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30)


    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(ExtendedCreationForm, self).save(commit=False)
        user.username = gen_login()  # Może by tak generować login na formularzu, żeby user też go widział?

        if commit:
            user.save()
        return user
