from django.urls import path, include
from rest_framework import routers

from .views import \
    MachineGETListView, MachinePOSTView, MachineSearchView, \
    MachinePUTView, MachineViewSet, MaintenanceGETListView, \
    MaintenanceSearchView, MaintenancePOSTView, MaintenancePUTView, \
    MaintenanceViewSet, ComplaintViewSet, ComplaintGETListView, \
    ComplaintSearchView, ComplaintPOSTView, ComplaintPUTView


router = routers.SimpleRouter()
router.register(r'machine', MachineViewSet, basename='machine')
router.register(r'maintenance', MaintenanceViewSet, basename='maintenance')
router.register(r'complaint', ComplaintViewSet, basename='complaint')

urlpatterns = [
    path('', include(router.urls)),

    # path('get_machine', MachineGETListView.as_view()),
    # path('get_machine/<int:pk>', MachineSearchView.as_view()),
    path('post_machine', MachinePOSTView.as_view()),
    path('put_machine/<int:pk>', MachinePUTView.as_view()),

    # path('get_maintenance', MaintenanceGETListView.as_view()),
    # path('get_maintenance/<int:pk>', MaintenanceSearchView.as_view()),
    path('post_maintenance', MaintenancePOSTView.as_view()),
    path('put_maintenance/<int:pk>', MaintenancePUTView.as_view()),

    # path('get_complaint/', ComplaintGETListView.as_view()),
    # path('get_complaint/<int:pk>/', ComplaintSearchView.as_view()),
    path('post_complaint', ComplaintPOSTView.as_view()),
    path('put_complaint/<int:pk>', ComplaintPUTView.as_view()),

]
