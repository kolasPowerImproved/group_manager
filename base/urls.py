from django.urls import path

from base import views
from base.views import index

urlpatterns = [
    path('/', views.index, name='index'),
    path('/group/<group_name>', views.group_detail, name='group_detail')
]