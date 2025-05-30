from django.shortcuts import render, redirect


def offerta_view(request):
    return render(request, 'mpd_offerta.html')


def privacy_policy(request):
    return render(request, 'mpd_privacy_policy.html')
# Create your views here.


def home(request):
    return render(request, 'home.html')