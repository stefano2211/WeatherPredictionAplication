from django import forms


class ModelForm(forms.Form):
    temp_max = forms.DecimalField(
        label='Max Temperature(C)', decimal_places=2, max_digits=4, widget=forms.TextInput(attrs={'class': 'form-control'}))
    temp_min = forms.DecimalField(
        label='Min Temperature (C)', decimal_places=2, max_digits=4, widget=forms.TextInput(attrs={'class': 'form-control'}))
    wind = forms.DecimalField(
        label='Wind', decimal_places=2, max_digits=4, widget=forms.TextInput(attrs={'class': 'form-control'}))
