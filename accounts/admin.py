from django.contrib import admin
from accounts.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'phone', 'institution')

admin.site.register(Profile, ProfileAdmin)
