from django.contrib import admin
from .models import MessageModel

@admin.register(MessageModel)

class MessageModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    ordering = ('-created_at',)