from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile
from django import forms

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        # help_text=password_validation.password_validators_help_text_html(),
    )

    class Meta:
        model = UserProfile
        fields = ('name', 'email', 'phone_number', 'address', 'postal_code', 'city',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
                "autofocus"
            ] = True

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    # password1 = forms.CharField(
    #     label=("Password"),
    #     strip=False,
    #     widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    #     # help_text=password_validation.password_validators_help_text_html(),
    # )

    class Meta:
        model = UserProfile
        fields = ('name', 'email', 'phone_number', 'address', 'postal_code', 'city',)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if self._meta.model.USERNAME_FIELD in self.fields:
    #         self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
    #             "autofocus"
    #         ] = True

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data["password1"])
    #     if commit:
    #         user.save()
    #     return user