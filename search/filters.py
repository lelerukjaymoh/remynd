import django-filters
from .models import search

class searchFilter(django-filters.FilterSet):

    class Meta:
        model = search
        fields = ('search_item',)
