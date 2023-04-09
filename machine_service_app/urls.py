from django.urls import path, include
from .views import \
    MachineGETListView, MaintenanceView, ComplaintView, \
    MachinePOSTView, MachineSearchView, MachinePUTView, \
    MachineViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'machine', MachineViewSet, basename='machine')

urlpatterns = [
    path('api/v1/', include(router.urls)),

    path('get_machine', MachineGETListView.as_view()),
    path('get_machine/<int:pk>', MachineSearchView.as_view()),
    path('post_machine', MachinePOSTView.as_view()),
    path('put_machine/<int:pk>', MachinePUTView.as_view()),
    path('maintenance', MaintenanceView.as_view()),
    path('complaints', ComplaintView.as_view()),
]
