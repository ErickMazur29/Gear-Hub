from django.contrib import admin
from accounts.models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display  = ('user','age', 'gender', 'phone')
    search_fields = ('user',)

admin.site.register(Profile, ProfileAdmin)
