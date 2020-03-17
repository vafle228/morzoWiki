from django import forms
from .models import dbMorzo

class MorzoForm(forms.ModelForm):
	string = forms.CharField(widget=forms.Textarea)

	class Meta():
		model = dbMorzo
		fields = ['string']