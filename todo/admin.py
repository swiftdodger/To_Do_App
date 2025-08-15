from django.contrib import admin
from django.utils.html import format_html
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status_badge', 'created_at')
    list_filter = ('completed', 'created_at')
    search_fields = ('title', 'description')
    actions = ['mark_completed', 'mark_not_completed']

    def status_badge(self, obj):
        if obj.completed:
            return format_html('<span style="color: white; background: green; padding: 4px 8px; border-radius: 4px;">Completed</span>')
        return format_html('<span style="color: white; background: orange; padding: 4px 8px; border-radius: 4px;">Not Completed</span>')
    status_badge.short_description = "Status"

    @admin.action(description="Mark selected tasks as completed")
    def mark_completed(self, request, queryset):
        updated = queryset.update(completed=True)
        self.message_user(request, f"{updated} task(s) marked as completed.")

    @admin.action(description="Mark selected tasks as not completed")
    def mark_not_completed(self, request, queryset):
        updated = queryset.update(completed=False)
        self.message_user(request, f"{updated} task(s) marked as not completed.")
