from django import forms

from .models import Planer
from PhoneBook.models import Contact

class PlanerForm(forms.ModelForm):
    contact = forms.ModelChoiceField(
        label="Контакт",
        widget=forms.Select(attrs={"class": "form-select"}),
        queryset=Contact.objects.none()
    )
    title = forms.CharField(
        label="Тема зустрічі",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    description = forms.CharField(
        label="Додаткова інформація (необов'язково)",
        required=False
    )
    date = forms.DateTimeField(
        label="Дата та час зустрічі",
        input_formats=["%Y-%m-%dT%H:%M"],
        widget=forms.DateTimeInput(attrs={
            "class": "form-control",
            "type": "datetime-local"
        })
    )
    url = forms.URLField(
        label="Посилання на зустріч (необов'язково)",
        widget=forms.URLInput(attrs={"class": "form-control"}),
        required=False
    )
    place = forms.CharField(
        label="Місце зустрічі",
        initial="Онлайн",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Planer
        exclude = ["user, accept"]