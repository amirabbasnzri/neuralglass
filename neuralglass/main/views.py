from django.shortcuts import render
from .forms import MessageForm
from .models import SocialLink, ContactText

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
    
    context = {
       'form': form,
       'success': success,  
       'links': links,
       'contact_text': contact_text 
              }
         
    return render(request, 'main/main.html', context)


