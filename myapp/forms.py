from django import forms
from .models import thumb
class ThumbForm(forms.Form):
	youtube_url=forms.CharField(max_length=200, widget= forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'urlid'}))
	class Meta:
		model =thumb
		fields = ('__all__')
