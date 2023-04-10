from django.contrib.auth.models import User
from django.contrib import auth
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect

from accounts_app.models import Customer
from .serializers import UserSerializer, UserCustomerSerializer


@method_decorator(csrf_protect, name='dispatch')
class CheckAuthenticatedView(APIView):
    def get(self, request, format=None):
        try:
            is_authenticated = User.is_authenticated

            if is_authenticated:
                return Response({'isAuthenticated': 'success'})
            else:
                return Response({'isAuthenticated': 'error'})
        except IOError:
            return Response({'error': 'Ошибка аутентификации'})


@method_decorator(csrf_protect, name='dispatch')
class SignupView(APIView):
    permission_classes = (permissions.IsAdminUser, )

    def post(self, request, format=None):
        data = self.request.data

        username = data['username']
        password = data['password']
        re_password = data['re_password']
        #  group

        try:
            if password == re_password:
                if User.objects.filter(username=username).exists():
                    return Response({'error': 'Такой пользователь уже есть.'})
                else:
                    if len(password) < 6:
                        return Response({'error': 'Пароль должен быть не менее 6 знаков'})
                    else:
                        user = User.objects.create_user(username=username, password=password)

                        user.save()
                        user = User.objects.get(id=user.id)

                        user_profile = Customer(user=user, group='Пользователь')
                        user_profile.save()

                        return Response({'success': 'Пользователь успешно создан'})
            else:
                return Response({'error': 'Пароли не совпадают'})

        except IOError:
            return Response({'error': 'Ошибка создания пользователя'})


@method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data
        print(data)
        username = data['username']
        password = data['password']

        try:
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return Response({'success': 'Пользователь авторизован', 'username': username})
            else:
                return Response({'error': 'Ошибка авторизации'})
        except IOError:
            return Response({'error': 'Ошибка авторизации'})


class LogoutView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        try:
            auth.logout(request)
            return Response({'success': 'Пользователь деавторизован'})
        except IOError:
            return Response({'error': 'Ошибка деавторизации'})


@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        return Response({'success': 'CSRF Cookie готов'})


@method_decorator(csrf_protect, name='dispatch')
class DeleteAccountView(APIView):
    permission_classes = (permissions.IsAdminUser, )

    def delete(self, request, format=None):
        user = self.request.user

        try:
            user = User.objects.filter(id=user.id).delete()

            return Response({'success': 'Пользователь удалён успешно'})
        except IOError:
            return Response({'error': 'Ошибка удаления пользователя'})


# @method_decorator(csrf_protect, name='dispatch')
class GetUsersView(APIView):
    permission_classes = (permissions.IsAdminUser, )

    def get(self, request, format=None):
        users = User.objects.all()

        users = UserSerializer(users, many=True)
        return Response(users.data)


# @method_decorator(csrf_protect, name='dispatch')
class GetUserCustomerView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):

        try:
            user = self.request.user
            username = user.username

            user = User.objects.get(id=user.id)

            user_profile = Customer.objects.get(user=user)
            user_profile = UserCustomerSerializer(user_profile)

            return Response({'profile': user_profile.data, 'username': str(username)})

        except IOError:
            return Response({'error': 'Ошибка обновления пользователя'})


@method_decorator(csrf_protect, name='dispatch')
class UpdateUserProfileView(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def put(self, request, format=None):

        user = self.request.user
        username = user.username

        data = self.request.data
        print(data)
        group = data['group']

        try:

            user = User.objects.get(id=user.id)

            Customer.objects.filter(user=user).update(group=group)

            user_profile = Customer.objects.get(user=user)
            user_profile = UserCustomerSerializer(user_profile)

            return Response({'profile': user_profile.data, 'username': str(username)})

        except IOError:
            return Response({'error': 'Ошибка обновления пользователя'})
