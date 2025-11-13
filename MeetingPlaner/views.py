from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.contrib import messages

from .models import Planer
#form PhoneBook.models import Contact
from .forms import PlanerForm, Contact



@login_required
def add_planer(request: HttpRequest):
    form = PlanerForm()
    if request.method == "POST":
        form = PlanerForm(request.POST)
        if form.is_valid():
            planer = form.save(commit=False)
            planer.user = request.user
            planer.save()
        messages.add_message(request, messages.SUCCESS, "Зустріч успішно cтворена")
        return redirect("get_planners")

    form.fields=["contact"].queryset = Contact.objects.filter(user=request.user).all()
    return render(request, "add_planer.html", dict(form=form))


@login_required
def get_my_planers(request: HttpRequest):
    planers = Planer.objects.filter(user=request.user).all()
    return render(request, "my_planers.html", dict(planers=planers))


@login_required
def get_planers_for_me(request: HttpRequest):
    planers = Planer.objects.filter(contact__user=request.user.first_name, contact__last_name=request.user.last_name).all()
    return render(request, "planers_for_me.html", dict(planers=planers))


