from django.forms import ModelForm, TextInput, Textarea, FileInput
from .models import Receta

class RecetaForm(ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo','detalle','ingredientes','imagen'] 
        widgets = {
            'titulo': TextInput(attrs={
                'class': "form-controll",
                }),
            'detalle': Textarea(attrs={
                'class': "form-controll", 
                }),
            'ingredientes': Textarea(attrs={
                'class': "form-controll", 
                }),
            'imagen': FileInput(attrs={
                'class': "form-controll", 
                })    
        }
class RecetaDeleteForm(ModelForm):
    class Meta:
        model = Receta
        fields = []