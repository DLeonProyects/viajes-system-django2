from django.forms import ModelForm

from webapp.models import Viajess


class viajeForm(ModelForm):
    class Meta:
        model = Viajess # El modelo subyacente del formulario es "Viajess"
        fields = '__all__' # Todos los campos del modelo se incluirán en el formulario

        #widgets = {
        #    'email': EmailInput(attrs={'type': 'email'})
        #}
