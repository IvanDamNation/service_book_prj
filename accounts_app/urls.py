from django.urls import path, include
from .views import \
    SignupView, GetCSRFToken, LoginView, \
    LogoutView, DeleteAccountView, GetUsersView, \
    GetUserCustomerView, UpdateUserProfileView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('user', GetUserCustomerView.as_view()),
    path('update', UpdateUserProfileView.as_view()),
    path('register', SignupView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('delete', DeleteAccountView.as_view()),
    path('csrf_cookie', GetCSRFToken.as_view()),
    path('get_users', GetUsersView.as_view()),
]
