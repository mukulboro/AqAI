from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth import authenticate, login
from . import forms

def admin_login(request):
    if request.method == "GET":
        form = forms.AdminLoginForm()
        ctx = {
            "form": form
        }
        return render(request, "login.html", context=ctx)
    elif request.method == "POST":
        form = forms.AdminLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(username=email, password=password)
            if user is None:
                messages.error(request, message="Invalid Credentials")
                return redirect("/login")
            elif user.is_municipal == True:
                login(request, user)
                return redirect("/dashboard")
            else:
                messages.error(request, "You do not have access to this part of the website")
                return redirect("/login")                
        else:
            messages.error(request, form.errors)
            return redirect("/login")
    else:
        redirect("403")

def dasboard_start(request):
    if request.user.is_municipal:
        context = {
            "email": request.user.email,
            "name": f"{request.user.first_name} {request.user.middle_name} {request.user.last_name}"
        }
        return render(request, "dashboard_one.html", context=context)
    else:
        messages.error(request, "You do not have access to this part of the website")
        return redirect("/login")