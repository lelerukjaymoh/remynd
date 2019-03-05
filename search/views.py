from django.shortcuts import render
from .models import search
from django.utils import timezone
from .forms import searchForm

def index(request):
	return render(request, 'index.html')

def search_list(request):
    searchs = search.objects.all()
    return render(request, 'index.html', {'searchs': searchs})

def new_search(request):
    form = searchForm()
    return render(request, 'index.html', {'form': form})
