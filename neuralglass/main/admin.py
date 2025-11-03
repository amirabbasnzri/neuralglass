from django.contrib import admin
from .forms import SectionForm
from django.contrib.auth.models import Group
from .models import SiteInfo,Stat, MessageModel, SocialLink, ContactText, Section, Section1, Section2, Section3, FooterInfo
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.db.models.signals import post_migrate
from django.dispatch import receiver


admin.site.unregister(Group)

# edit_admin_login_panel:
try:
    site_info = SiteInfo.objects.first()
    site_name = site_info.site_name if site_info else "Admin"
except:
    site_name = "Admin"
admin.site.site_header = f'{site_name} Adminetrtion'
admin.site.site_title = f'{site_name} Portal'
admin.site.index_title = f'Welcome to {site_name} Administration'

# -----------------------------------------------------------------------------------------------------------------

# site_info:
@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if SiteInfo.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Stat.objects.count() >= 6:
            return False
        return super().has_add_permission(request)

# -----------------------------------------------------------------------------------------------------------------

# messages:
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

# ---------------------------------------------------------------------------------------------------------------


# contact:
@admin.register(SocialLink)
class SocialLinksAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    
    def has_add_permission(self, request):
        if SocialLink.objects.count() >= 4:
            return False
        return super().has_add_permission(request)
    
    def get_changelist_instance(self, request):
        return super().get_changelist_instance(request)

    
    def add_view(self, request, form_url='', extra_context=None):
        if not self.has_add_permission(request):
            self.message_user(request, "You cannot create more than 4 records.", level=messages.ERROR)
            return redirect(reverse('admin:main_sociallink_changelist'))
        return super().add_view(request, form_url, extra_context)
    
@admin.register(ContactText)
class ContactTextAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not ContactText.objects.exists()
    def has_delete_permission(self, request, obj=None):
        return False

# ----------------------------------------------------------------------------------------------------------------


# sections:
@receiver(post_migrate)
def create_default_sections(sender, **kwargs):
    if sender.name == 'main': 
        for i in range(1, 4): 
            Section.objects.get_or_create(id=i, defaults={'section_name': str(i), 'order': int(i)})  
  
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    form = SectionForm
    list_display = ('section_name', 'order')
    
    def has_add_permission(self, request):
        if Section.objects.count() >= 3:
            return False
        return super().has_add_permission(request)

@admin.register(Section1)
class Section2Admin(admin.ModelAdmin):
    
    def has_add_permission(self, request):
        if Section1.objects.count() >= 4:
            return False
        return super().has_add_permission(request)

@admin.register(Section2)
class Section3Admin(admin.ModelAdmin):
    list_display = ('title', 'emoji', 'description')
    
    def has_add_permission(self, request):
        if Section2.objects.count() >= 10:
            return False
        return super().has_add_permission(request)
    
    def get_changelist_instance(self, request):
        cl = super().get_changelist_instance(request)
        if Section2.objects.count() >= 10 and not self.has_add_permission(request):
            messages.error(request, "You've already created 10 records")
        return cl
    
    def add_view(self, request, form_url='', extra_context=None):
        if not self.has_add_permission(request):
            self.message_user(request, "You cannot create more than 10 records.", level=messages.ERROR)
            return redirect(reverse('admin:main_matrixprotocol_changelist'))
        return super().add_view(request, form_url, extra_context)

@admin.register(Section3)
class Section4Admin(admin.ModelAdmin):
    
    def has_add_permission(self, request):
        if Section3.objects.count() >= 4:
            return False
        return super().has_add_permission(request)

# ----------------------------------------------------------------------------------------------------------------


# footer:
@admin.register(FooterInfo)
class FooterInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not FooterInfo.objects.exists()
    def has_delete_permission(self, request, obj=None):
        return False

# ----------------------------------------------------------------------------------------------------------------