from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Contact
from .forms import ContactForm, FilterForm


# Create your views here.

@login_required
def add_contact(request: HttpRequest):
    form = ContactForm(data=request.POST or None, files=request.FILES or None)
    if request.method == "POST" and form.is_valid():
        contact: Contact = form.save(commit=False)
        contact.user = request.user
        contact.save()
        messages.add_message(request=request, level=messages.SUCCESS, message="Контакт успішно додано.")
        return redirect("get_contacts")

    return render(request, "add_contact.html", dict(form=form))


@login_required
def get_contacts(request: HttpRequest):
    contacts = Contact.objects.filter(user=request.user).all()
    return render(request, "contacts.html", dict(contacts=contacts))


@login_required
def remove_contact(request: HttpRequest, contact_id: int):
    contact = Contact.objects.filter(pk=contact_id, user=request.user).first()
    contact.delete()
    messages.add_message(request=request, level=messages.SUCCESS, message=f"Контакт '{contact}' було успішно видалено.")
    return redirect("get_contacts")


@login_required
def update_contact(request: HttpRequest, contact_id: int):
    contact = Contact.objects.filter(pk=contact_id, user=request.user).first()
    form = ContactForm(data=request.POST or None, files=request.FILES or None, instance=contact)
    if request.method == "POST" and form.changed_data():
        form.save()
        messages.add_message(request=request, level=messages.SUCCESS, message="Контакт '{contact}' успішно оновлено.")
        return redirect("get_contacts")

    return render(request, "edit_contact.html", dict(form=form))


@require_POST
@login_required
def filter_contacts(request: HttpRequest):
    form = FilterForm(data=request.POST)
    if form.is_valid():
        contacts = (Contact.objects
            .filter(first_name__icontains=form.cleaned_data["first_name"])
            .filter(last_name__icontains=form.cleaned_data["last_name"])
            .filter(phone_number__icontains=form.cleaned_data["phone_number"])
            .filter(email__icontains=form.cleaned_data["email"])
            .filter(address__icontains=form.cleaned_data["address"])
            .filter(user=request.user)
        ).all()
        return render(request, "contacts.html", dict(contacts=contacts, form=FilterForm()))

        