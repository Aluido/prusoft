from django.forms import ModelForm
from .models import Receta

class RecetaForm(ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo','detalle','ingredientes','imagen'] 

class RecetaDeleteForm(ModelForm):
    class Meta:
        model = Receta
        fields = []