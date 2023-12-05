from django import forms
from .models import atalaiashouse
from pprint import pprint

class cadastro(forms.ModelForm):
    class meta:
        model = atalaiashouse
        fields = ("__all__")
        exclude = ('codClients')

    def __init__(self, *args, **kwargs):
        super(cadastro, self).__init__(*args, **kwargs)
        for field in self.fields:
             self.fields[field].widget.attrs.update({
		    'class': 'form-control'})
  
