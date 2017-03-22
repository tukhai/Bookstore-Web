from django.shortcuts import render

from .models import Book

# Create your views here.

def index(request):
    return render(request, 'template.html')

def store(request):
    count = Book.objects.all().count()
    context = {
        'count': count,
    }
    
    if request.user.is_authenticated():
        request.session['location'] = "Earth"
    else:
        request.session['location'] = "unknown" 
        
    return render(request, 'store.html', context)


