from django.urls import path
from base.views import GroupsList

urlpatterns = [
    path('publishers/', GroupsList.as_view()),
]