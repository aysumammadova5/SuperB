from django import forms 
from .models import Comment 
from django.forms import Textarea, TextInput

class CommentForm(forms.ModelForm):    
    class Meta:        
        model = Comment        
        fields = ('name','email','comment')        
        widgets = { 'name': forms.TextInput(attrs={'class':'form-control'}),            
                    'email': forms.EmailInput(attrs={ 'class':'form-control'}),                 
                    'comment': forms.Textarea(attrs={ 'class':'form-control','rows':5,"cols":50}),
                    }