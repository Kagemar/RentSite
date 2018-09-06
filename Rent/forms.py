from django import forms
from .models import Ad


class AdForm(forms.ModelForm):
    localization = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id': "autocomplete"}))

    class Meta:
        model = Ad
        fields = ('title', 'text', 'localization', 'surface', 'rooms', 'floor',)
