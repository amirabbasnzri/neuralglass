from .models import FooterInfo, Section

def footer_context(request):
    return {
        'footer_info': FooterInfo.objects.first()
    }
    
def section_context(request):
    return {
        'section': Section.objects.order_by('id').all()
    }
    
def site_info_context(request):
    return {
        'site_info': Section.objects.first()
    }