from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from base.models import Group, Child, Trainer


class GroupsList(ListView):
    model = Group


def index(request):
    if request.method == 'GET':
        groups = Group.objects.all()
        children = Child.objects.all()
        children_count = Group.objects.count()
        trainers = Trainer.objects.all()
        return render(request, 'index.html', {'groups': groups,
                                              'children': children,
                                              'trainers': trainers,
                                              'children_count': children_count})
    else:
        return render(request, 'index.html')