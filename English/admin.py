from django.contrib import admin

from English.models import Author


# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "year_of_birth")
    list_filter = ("first_name", "year_of_birth")

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Author, AuthorAdmin)
