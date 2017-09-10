from django.contrib import admin
from service_study.models import Notice, Attendance


class NoticeAdmin(admin.ModelAdmin):
    list_display = ('study', 'upload_time', 'contents')


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'study', 'date', 'status')


admin.site.register(Notice, NoticeAdmin)
admin.site.register(Attendance, AttendanceAdmin)
