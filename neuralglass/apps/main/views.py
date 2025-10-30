from django.shortcuts import render
from .forms import MessageForm

def main(request):
    print('request recived')
    if request.method == 'POST':
        print('data has been sent')
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MessageForm()
            
    return render(request, 'main/main.html', {'form': form})


