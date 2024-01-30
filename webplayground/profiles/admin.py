from django.contrib import admin
from registration.models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    #onlye have 4 items, user, avatar, bio and link
    list_display = ('user', 'avatar', 'bio', 'link')


admin.site.register(Profile, ProfileAdmin)