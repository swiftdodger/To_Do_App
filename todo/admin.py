from django.contrib import admin
from todo.models import Task

# Register your models here.

@admin.register(Task)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed_at')
    list_filter = ('completed_at',)
    search_fields = ('title',)

