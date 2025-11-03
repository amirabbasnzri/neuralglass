from django.shortcuts import render
from .forms import MessageForm
from .models import SiteInfo, Stat, SocialLink, ContactText, Section, Section1, Section2, Section3

def main(request):
    success = False
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = MessageForm()
    
    site_info = SiteInfo.objects.first()
    stats = Stat.objects.all()
    links = SocialLink.objects.filter(is_active=True).order_by('order')[:4]
    contact_text = ContactText.objects.last()
    section1 = Section1.objects.all()
    section2 = Section2.objects.all()
    section3 = Section3.objects.order_by('year').all()
    s1 = Section.objects.get(id=1)
    s2 = Section.objects.get(id=2)
    s3 = Section.objects.get(id=3)
    
    context = {
       'site_info': site_info,
       'stats': stats, 
       'form': form,
       'success': success,  
       'links': links,
       'contact_text': contact_text,
       'section1': section1,
       'section2': section2,
       'section3': section3,
       's1': s1,
       's2': s2,
       's3': s3
              }
         
    return render(request, 'main/main.html', context)


