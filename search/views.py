from django.shortcuts import render
from .models import search
from django.utils import timezone

def index(request):
	return render(request, 'index.html')

def search_list(request):
    searchs = search.objects.all()
    return render(request, 'index.html', {'searchs': searchs})
	
