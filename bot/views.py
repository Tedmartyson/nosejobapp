from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return HttpResponse("<h1>Hello, Dinka Koren</h1>")


def webhook(request):
    return HttpResponse("test")
