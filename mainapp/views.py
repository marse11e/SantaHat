from django.shortcuts import render
from .models import PhotoEdit



def index(request):
    photo = PhotoEdit.objects.all()
    
    context = {
        'context_photo' : photo,
    }
    return render(request, 'index.html', context)
