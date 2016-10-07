from django import forms

from app.aldea.models import Aldea

class AldeaForm(forms.ModelForm):

	class Meta:
		model = Aldea

		fields = [
		'nombre',
		#'departamento',
			]

		labels= {

		'nombre': 'Nombre',
		#'departamento': 'Departamento',
		
		}

		widgets= {
        'nombre': forms.TextInput(attrs={'class':'form-control'}),
		#'departamento': forms.Select(attrs={'class':'form-control'}),
		}