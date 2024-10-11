from django.urls import path
from . import views

urlpatterns = [
    path("hoopview/", views.hoopview),
    path("halloumi", views.halloumi)
]