import time

from django.shortcuts import render, redirect
from django.contrib import messages

from django_rq import job

from .models import Secret

# https://github.com/rq/django-rq#job-decorator
@job
def generate_bg():
    time.sleep(2) # Simulate expensive operation.
    Secret.objects.create()


def index(request):
    context = {'secrets': Secret.objects.all()}
    return render(request, 'fizuapp/index.html', context)


def blank(request):
    context = {'secrets': Secret.objects.all()}
    return render(request, 'fizuapp/blank.html', context)


def buttons(request):
    context = {'secrets': Secret.objects.all()}
    return render(request, 'fizuapp/buttons.html', context)


def cards(request):
    context = {'secrets': Secret.objects.all()}
    return render(request, 'fizuapp/cards.html', context)


def charts(request):
    context = {'secrets': Secret.objects.all()}
    return render(request, 'fizuapp/charts.html', context)


def forgot_password(request):
    context = {'secrets': Secret.objects.all()}
    return render(request, 'fizuapp/forgot_password.html', context)


def login(request):
    context = {'secrets': Secret.objects.all()}
    return render(request, 'fizuapp/login.html', context)


def register(request):
    context = {'secrets': Secret.objects.all()}
    return render(request, 'fizuapp/register.html', context)


def tables(request):
    context = {'secrets': Secret.objects.all()}
    return render(request, 'fizuapp/tables.html', context)


def utilities_animation(request):
    context = {'secrets': Secret.objects.all()}
    return render(request, 'fizuapp/utilities_animation.html', context)


def utilities_border(request):
    context = {'secrets': Secret.objects.all()}
    return render(request, 'fizuapp/utilities_border.html', context)


def utilities_color(request):
    context = {'secrets': Secret.objects.all()}
    return render(request, 'fizuapp/utilities_color.html', context)


def utilities_other(request):
    context = {'secrets': Secret.objects.all()}
    return render(request, 'fizuapp/utilities_other.html', context)


def generate(request):
    if request.GET.get('bg'):
        generate_bg.delay()
        messages.success(request, 'Generating new key in background. Refresh page after two seconds to see generated key.')
    else:
        Secret.objects.create()
        messages.success(request, 'Generated new key.')
    return redirect('home')


def delete(request):
    Secret.objects.all().delete()
    messages.success(request, 'Deleted all keys.')
    return redirect('home')
