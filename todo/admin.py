from django.contrib import admin
from django.utils.html import format_html
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status_badge', 'created_at', 'completed_at')
    list_filter = ('completed_at',)  # filter by completion date

    def status_badge(self, obj):
        if obj.completed_at:
            return format_html(
                '<span style="color: white; background: green; padding: 4px 8px; border-radius: 4px;">Completed</span>'
            )
        return format_html(
            '<span style="color: white; background: orange; padding: 4px 8px; border-radius: 4px;">Not Completed</span>'
        )
    status_badge.short_description = "Status"
