from django import forms 
from .models import Review

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['price_review', 'value_review', 'quality_review', 'name', 'summary', 'product_review']