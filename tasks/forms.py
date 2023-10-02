
# se va  acrear un formulario a partir de la tabla de Task
# una clase que me permite externderla
from django.forms import ModelForm 

from .models import Task

class NewTask_form(ModelForm):
    class Meta:
        model= Task
        fields= [
            'titulo',
            'descripcion',
            'es_importante'
        ]