from django.contrib import admin
from service_main.models import Study, StudyUser, StudyRequest


class StudyAdmin(admin.ModelAdmin):
    list_display = ('title', 'deposit', 'url', 'admin')


class StudyUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'study', 'fine', 'deposit_pay')


class StudyRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'study', 'approval')


admin.site.register(Study, StudyAdmin)
admin.site.register(StudyUser, StudyUserAdmin)
admin.site.register(StudyRequest, StudyRequestAdmin)
