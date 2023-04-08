import allauth
import rest_framework
import django.apps
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from accounts_app.models import FactoryManager, ServiceManager, Customer

# FactoryManager
# ServiceManager
# Customer

# admin.site.unregister(User)
# admin.site.unregister(django.contrib.auth.models.Group)

# admin.site.unregister(allauth.account.models.EmailAddress)
# admin.site.unregister(rest_framework.authtoken.models.TokenProxy)
# admin.site.unregister(allauth.socialaccount.models.SocialApp)
# admin.site.unregister(allauth.socialaccount.models.SocialAccount)
# admin.site.unregister(allauth.socialaccount.models.SocialToken)

# admin.site.register(User, AccountsUserAdmin)

admin.site.register(FactoryManager)
admin.site.register(ServiceManager)
admin.site.register(Customer)
