from django import forms
from .models import search

class searchForm(forms.ModelForm):

    class Meta:
        model = search
        fields = ('search_item',)
