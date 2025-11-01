from django.shortcuts import render
from .forms import MessageForm

def main(request):
    success = False
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = MessageForm()
        
    context = {
        'form': form,
        'success': success,       
               }
            
    return render(request, 'main/main.html', context)


