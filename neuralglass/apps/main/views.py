from django.shortcuts import render
from .forms import MessageForm

def main(request):
    print(request.method)
    if request.method == 'POST':
        form = MessageForm
        if form.is_valid():
            form.save()
    else:
        form = MessageForm
            
    return render(request, 'main/main.html', {'form': form})


