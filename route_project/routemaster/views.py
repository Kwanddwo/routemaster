from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User
# from .forms import ListingFormz

import os
maps_api_key = os.environ.get('MAPS_API_KEY')

# TODO: Put these views into different python modules if possible

@login_required
def index(request):
    return render(request, "routemaster/index.html")

# Authentification / User view
def user_view(request, username):
    user = User.objects.get(username=username)
    return render(request, "routemaster/user.html", {
        "user": user
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "routemaster/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "routemaster/login.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "routemaster/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "routemaster/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "routemaster/register.html")
    
@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))