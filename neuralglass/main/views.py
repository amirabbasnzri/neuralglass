from django.shortcuts import render
from .forms import MessageForm
from .models import SocialLink, ContactText, Section2, Section3, Section4

def main(request):
    success = False
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = MessageForm()
        
    links = SocialLink.objects.filter(is_active=True).order_by('order')[:4]
    contact_text = ContactText.objects.last()
    section2 = Section2.objects.all()
    section3 = Section3.objects.all()
    section4 = Section4.objects.order_by('year').all()
    
    
    context = {
       'form': form,
       'success': success,  
       'links': links,
       'contact_text': contact_text,
       'section2': section2,
       'section3': section3,
       'section4': section4
              }
         
    return render(request, 'main/main.html', context)


