from django.urls import path

from base import views
from base.views import index

urlpatterns = [
    path('/', views.index),
]