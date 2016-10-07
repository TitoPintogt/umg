from django import forms

from app.aldea.models import Aldea

class AldeaForm(forms.ModelForm):

	class Meta:
		model = Aldea

		fields = [
		'nombre',
		'municipio',
			]

		labels= {

		'nombre': 'Nombre',
		'municipio': 'Municipio',
		
		}

		widgets= {
        'nombre': forms.TextInput(attrs={'class':'form-control'}),
		'municipio': forms.Select(attrs={'class':'form-control'}),
		}