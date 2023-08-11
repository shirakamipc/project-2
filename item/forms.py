from django import forms
from .models import Item
from django.core.exceptions import ValidationError

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

        def clean_image(self):
            image = self.cleaned_data.get('image')
            if not image:
                raise ValidationError("You must select an image for the item.")
            return image

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
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