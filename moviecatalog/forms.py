from django import forms

class Genre_Quiz(forms.Form):
  nota = forms.IntegerField(label="Nota:", min_value=0, max_value=6)