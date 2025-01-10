from django.contrib import admin
from .models import ApiEndpoint

@admin.register(ApiEndpoint)
class ApiEndpointAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'status', 'last_checked')
    search_fields = ('name', 'url')
    
    