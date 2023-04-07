import allauth
import rest_framework
import django.apps
from django.contrib import admin

from accounts_app.models import FactoryManager, ServiceManager, Customer

# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'author', 'title', 'category', 'created_at', 'updated_at', 'is_published')
#     list_display_links = ('id', 'title')
#     search_fields = ('title', 'author', 'content')
#     list_editable = ('is_published', )
#     list_filter = ('is_published', 'category')

# FactoryManager
# ServiceManager
# Customer

# admin.site.unregister(django.contrib.auth.models.User)
admin.site.unregister(django.contrib.auth.models.Group)
admin.site.unregister(allauth.account.models.EmailAddress)
admin.site.unregister(rest_framework.authtoken.models.TokenProxy)
admin.site.unregister(allauth.socialaccount.models.SocialApp)
admin.site.unregister(allauth.socialaccount.models.SocialAccount)
admin.site.unregister(allauth.socialaccount.models.SocialToken)

admin.site.register(FactoryManager)
admin.site.register(ServiceManager)
admin.site.register(Customer)
