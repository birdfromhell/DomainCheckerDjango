from django.urls import path
from . import views

urlpatterns = [
    path('', views.DomainChecker.as_view()),
]