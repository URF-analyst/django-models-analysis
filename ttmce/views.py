from django.shortcuts import render

# Create your views here.
from .models import message

def display (request):
    mssg = message.objects.all()
    context = {
        #'data':data,
        'mssg': mssg,

    }
    return render(request, 'info.html', context)
