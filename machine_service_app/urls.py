from django.urls import path, include
from rest_framework import routers

from .views import \
    MachineGETListView, MachinePOSTView, MachineSearchView, \
    MachinePUTView, MachineViewSet, MaintenanceGETListView, \
    MaintenanceSearchView, MaintenancePOSTView, MaintenancePUTView, \
    ComplaintView


router = routers.SimpleRouter()
router.register(r'machine', MachineViewSet, basename='machine')
router.register(r'maintenance', MachineViewSet, basename='maintenance')

urlpatterns = [
    path('api/v1/', include(router.urls)),

    path('get_machine', MachineGETListView.as_view()),
    path('get_machine/<int:pk>', MachineSearchView.as_view()),
    path('post_machine', MachinePOSTView.as_view()),
    path('put_machine/<int:pk>', MachinePUTView.as_view()),

    path('get_maintenance', MaintenanceGETListView.as_view()),
    path('get_maintenance/<int:pk>', MaintenanceSearchView.as_view()),
    path('post_maintenance', MaintenancePOSTView.as_view()),
    path('put_maintenance/<int:pk>', MaintenancePUTView.as_view()),

    path('complaints', ComplaintView.as_view()),
]
