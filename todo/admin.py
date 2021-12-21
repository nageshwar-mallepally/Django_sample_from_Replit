from django.contrib import admin
from .models import TodoItem



class TodoItemAdmin(admin.ModelAdmin):
    list_display = ["id", "content"]

admin.site.register(TodoItem, TodoItemAdmin)