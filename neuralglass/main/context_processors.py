from .models import FooterInfo

def footer_context(request):
    return {
        'footer_info': FooterInfo.objects.first()
    }