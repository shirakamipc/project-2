from django import forms
from .models import Item

INPUT_CLASSESS ='w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSESS
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSESS
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSESS
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSESS
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSESS
            })

        }
