from django.contrib import admin
from webapp.models import Visitor


class VisitorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'author', 'email', 'created_at', 'status']
    list_filter = ['author']
    list_display_links = ['pk', 'email']
    search_fields = ['email', 'text', 'status']
    fields = ['author', 'email', 'text', 'status']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Visitor, VisitorAdmin)
