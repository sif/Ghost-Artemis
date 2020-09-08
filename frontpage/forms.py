"""For forms for this app."""

from django import forms

from .models import Quotation

class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = ('quote', 'author')
        widgets = {
            'quote': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
        }
