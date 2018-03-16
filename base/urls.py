from django.conf.urls import url
from django.urls import path

from base import views
from base.views import index

urlpatterns = [
    path('/', views.index, name='index'),
    path('/group_list_api', views.group_list_api, name='group_list_api'),
    path('/group/<group_name>', views.group_detail, name='group_detail'),
    path('/group_detail_api/<group_name>', views.group_detail_api, name='group_detail_api'),
    path('/childs_detail_api/<group_name>', views.childs_detail_api, name='childs_detail_api'),
]