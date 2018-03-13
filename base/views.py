from django.db.models import QuerySet
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from base.models import Group, Child, Trainer
from base.serializers import GroupSerializer, ChildSerializer, TrainerSerializer


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


@csrf_exempt
def group_list(request):
    """
    List all groups, or create a new group
    :param request:
    :return:
    """
    if request.method == 'GET':
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GroupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def group_detail(request, pk):
    """
    Retrieve, update or delete a group
    :param request:
    :param pk:
    :return:
    """
    try:
        group = Group.objects.get(pk=pk)
    except Group.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = GroupSerializer(group)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = GroupSerializer(group, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        group.delete()
        return HttpResponse(status=204)