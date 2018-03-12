from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from base.models import Group, Child, Trainer


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


def group_detail(request, group_name):
    if request.method == 'GET':
        group = get_object_or_404(Group, group_name=group_name)
        girls = group.children.filter(gender='F').count()
        boys = group.children.filter(gender='M').count()
        female_children = get_object_or_404(Child, gender='F')
        #male_children = get_object_or_404(Child, gender='M')
        #count_of_children = children.coun
        context = {'group': group, 'boys': boys, 'girls': girls}
        return render(request, 'group_detail.html', context=context)
    else:
        return render(request, 'index.html')
