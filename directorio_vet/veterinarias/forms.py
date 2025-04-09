from django import forms
from .models import Veterinaria

class VeterinariaForm(forms.ModelForm):
    class Meta:
        model = Veterinaria
        fields = '__all__'
        widgets = {
            'servicios': forms.CheckboxSelectMultiple,
            # Si quieres un widget personalizado para el campo 'horario', puedes usar Textarea
            'horario': forms.Textarea(attrs={'rows': 5, 'cols': 50}),
        }

    # Si es necesario, puedes validar que el horario tenga un formato adecuado
    def clean_horario(self):
        horario = self.cleaned_data.get('horario')
        # Aquí puedes agregar validación si es necesario
        if not isinstance(horario, dict):
            raise forms.ValidationError("El formato del horario no es correcto.")
        return horario
