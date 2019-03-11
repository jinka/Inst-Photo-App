from django.shortcuts import render
from .models import Image
from django.contrib.auth.decorators import login_required


@login_required(login_url='/register/')
def home(request):
    context = {
        'posts': Image.objects.all()
    }
    return render(request,'insta/home.html',context)

def about(request):
    return render(request,'insta/about.html', {'title': 'About'})
