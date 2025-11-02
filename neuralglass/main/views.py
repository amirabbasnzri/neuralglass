from django.shortcuts import render
from .forms import MessageForm
from .models import SocialLink, ContactText, MatrixProtocol

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
    matrix_protocol = MatrixProtocol.objects.all()
    
    context = {
       'form': form,
       'success': success,  
       'links': links,
       'contact_text': contact_text,
       'matrix_protocol': matrix_protocol
              }
         
    return render(request, 'main/main.html', context)


