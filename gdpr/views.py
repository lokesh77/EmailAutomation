from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, GDPR. You're at the gdpr index.")