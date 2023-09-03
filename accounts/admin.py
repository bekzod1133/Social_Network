from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User


# Register your models here.
class InlineProfile(admin.StackedInline):
    model = Profile


admin.site.unregister(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'password']
    inlines = [InlineProfile]
