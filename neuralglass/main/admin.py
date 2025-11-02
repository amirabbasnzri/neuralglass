from django.contrib import admin
from .models import MessageModel, SocialLink, ContactText, MatrixProtocol
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

@admin.register(MessageModel)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    ordering = ('-created_at',)
    
    def has_change_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request):
        return False 
    def has_delete_permission(self, request, obj=None):
        return True
    
@admin.register(SocialLink)
class SocialLinksAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    
    def has_add_permission(self, request):
        if SocialLink.objects.count() >= 4:
            return False
        return super().has_add_permission(request)
    
    def get_changelist_instance(self, request):
        cl = super().get_changelist_instance(request)
        if SocialLink.objects.count() >= 4 and not self.has_add_permission(request):
            messages.error(request, "You've already created 4 records")
        return cl
    
    def add_view(self, request, form_url='', extra_context=None):
        if not self.has_add_permission(request):
            self.message_user(request, "You cannot create more than 4 records.", level=messages.ERROR)
            return redirect(reverse('admin:main_sociallink_changelist'))
        return super().add_view(request, form_url, extra_context)
    
admin.site.register(ContactText)

@admin.register(MatrixProtocol)
class MatrixProtocolAdmin(admin.ModelAdmin):
    list_display = ('title', 'emoji', 'description')
    
    def has_add_permission(self, request):
        if MatrixProtocol.objects.count() >= 10:
            return False
        return super().has_add_permission(request)
    
    def get_changelist_instance(self, request):
        cl = super().get_changelist_instance(request)
        if MatrixProtocol.objects.count() >= 10 and not self.has_add_permission(request):
            messages.error(request, "You've already created 10 records")
        return cl
    
    def add_view(self, request, form_url='', extra_context=None):
        if not self.has_add_permission(request):
            self.message_user(request, "You cannot create more than 10 records.", level=messages.ERROR)
            return redirect(reverse('admin:main_matrixprotocol_changelist'))
        return super().add_view(request, form_url, extra_context)

