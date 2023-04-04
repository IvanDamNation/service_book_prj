from django.urls import path
from .views import MachineView

urlpatterns = [
    path('api/', MachineView.as_view()),
]
