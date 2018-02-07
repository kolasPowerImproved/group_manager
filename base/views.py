from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from base.models import Group


class GroupsList(ListView):
    model = Group


def index(response):
    return HttpResponse("hello world")