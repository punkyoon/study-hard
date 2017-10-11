from django.contrib import admin
from service_study.models import Notice, Attendance, Fine


class NoticeAdmin(admin.ModelAdmin):
    list_display = ('study', 'upload_time', 'contents')


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'study', 'date', 'status')


class FineAdmin(admin.ModelAdmin):
    list_display = ('user', 'study', 'date', 'fine_rate', 'fine_reason', 'fine_pay')


admin.site.register(Notice, NoticeAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Fine, FineAdmin)