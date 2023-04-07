from django.urls import path
from .views import MachineGETView, MaintenanceView, ComplaintView

urlpatterns = [
    path('machine/', MachineGETView.as_view()),
    path('maintenance/', MaintenanceView.as_view()),
    path('complaints/', ComplaintView.as_view()),
]
