from django.urls import path
from .views import MachineView, MaintenanceView, ComplaintView

urlpatterns = [
    path('machine/', MachineView.as_view()),
    path('maintenance/', MaintenanceView.as_view()),
    path('complaints/', ComplaintView.as_view()),
]
