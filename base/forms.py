from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField, UsernameField
from django.contrib.auth.models import User

from base.models import Profile

from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label=_("Email"), help_text=_("Enter valid email address"),)
    displayname = forms.CharField(label=_("Displayname"), help_text=_("Enter displayname"), required=False,)

    class Meta:
        model = User
        fields = ("username", "email", "displayname", "password1", "password2",)
        field_classes = {'username': UsernameField}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
            profile = Profile(display_name=self.cleaned_data["displayname"])
            profile.user = user
            profile.save()

            return user


class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(label=_("Email"), help_text=_("Enter a valid email address"), )
    displayname = forms.CharField(label=_("Displayname"), help_text=_("Enter displayname"), required=False, )

    password = ReadOnlyPasswordHashField(label=_("Password"),
                                         help_text=_("Raw passwords are not stored, so there's no way to see this"
                                                     "user's password, but you can change the password using "
                                                     "<a href=\"/accounts/password_change/\">this form</a>"))

    class Meta:
        model = User
        fields = ("username", "email", "displayname", "password")
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.profile = Profile.objects.get(user=self.instance)
        self.fields['displayname'].initial = self.profile.display_name
        f = self.fields.get('user_pemissions')

        if f is not None:
            f.queryset.select_related('content-type')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
            self.profile.display_name = self.cleaned_data["displayname"]
            self.profile.save()
            return user

    def clean_password(self):
        return self.initial["password"]
