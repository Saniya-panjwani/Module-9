from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ProfileForm, SignupForm
from .models import Profile


def home(request):
    return render(request, "index.html")


@login_required
def profile(request):
    return redirect("profile_edit")


@login_required
def profile_edit(request):
    profile_obj, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile_obj)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile_obj)

    return render(request, "profile_edit.html", {"form": form})


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create profile early so it exists
            Profile.objects.get_or_create(
                user=user,
                defaults={
                    "phone": form.cleaned_data.get("phone", ""),
                    "city": form.cleaned_data.get("city", ""),
                    "address": form.cleaned_data.get("address", ""),
                },
            )
            profile_obj, _ = Profile.objects.get_or_create(user=user)
            profile_obj.phone = form.cleaned_data.get("phone", "")
            profile_obj.city = form.cleaned_data.get("city", "")
            profile_obj.address = form.cleaned_data.get("address", "")
            profile_obj.save()

            login(request, user)
            return redirect("profile")
    else:
        form = SignupForm()

    return render(request, "registration/signup.html", {"form": form})

