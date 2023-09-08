from django.core.exceptions import ValidationError
from django import forms
from .models import Contact


class ContactForms(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        )
    )

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone',
                  'email', 'description', 'category',
                  'picture',)

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            error_msg = ValidationError(
                'Primeiro nome não pode ser igual ao sobrenome',
                code='invalid'
            )
            self.add_error('first_name', error_msg)
            self.add_error('last_name', error_msg)

        return super().clean()
