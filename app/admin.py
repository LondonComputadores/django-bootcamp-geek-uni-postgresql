from django.contrib import admin
from .models import Job, Service, Team


class JobAdmin(admin.ModelAdmin):
    list_display = ('job', 'active', 'modified_at')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service', 'icon', 'active', 'modified_at')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'modified_at', 'active', 'modified_at')

admin.site.register(Job, JobAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Team, TeamAdmin)