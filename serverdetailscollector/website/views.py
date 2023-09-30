from django.shortcuts import render
from devices.models import Device
from django.http import HttpResponse
from devices.functions import refresh_data
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

import csv


def home(request):
    devices = Device.objects.all()
    if request.user.is_authenticated:
        context = {"devices": devices}
        return render(request, "website/home.html", context=context)
    else:
        print("gi")
        return render(request, "website/index.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'user does not exist')
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        messages.error(request, 'incorrect password')
        return redirect('login')
    return redirect("home")


def user_logout(request):
    logout(request)
    return redirect("home")


def download(request):
    devices = Device.objects.all()
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="devices_details.csv"'},
    )
    writer = csv.writer(response)
    for device in devices:
        writer.writerow([device.hostname,
                         device.ip,
                         device.port,
                         device.system,
                         device.available_space,
                         device.free_space])

    return response


def refresh(request):
    refresh_data()
    return redirect("home")
