from django import forms

from .models import translate

class TranslateForm(forms.ModelForm):
    class Meta:
        model = translate
        fields = ('word', 'res')