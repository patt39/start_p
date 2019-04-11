from django.shortcuts import render
from .models import Article

def home(request):
    return render(request, 'darry/home.html',)

def about(request):
    return render(request, 'darry/about.html')

def pricing(request):
    return render(request, 'darry/pricing.html')

def contact(request):
    return render(request, 'darry/contact.html')

def work(request):
    context = {
        'articles': Article.objects.all()
    }
    return render(request, 'darry/work.html', context)

