from django import forms
from calfuan_diego_FINAL_APP.models import Inscritos
from calfuan_diego_FINAL_APP.models import Institucion

class FormInscritos(forms.ModelForm):
    class Meta:
        model = Inscritos
        fields = '__all__'

class FormInstitucion(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = '__all__'