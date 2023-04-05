from django.urls import path
from .views import MachineView

urlpatterns = [
    path('machine/', MachineView.as_view()),
]
