from django import forms

class EditProfileForm(forms.Form):
  bio = forms.CharField(label="Bio:")
  pic = forms.ImageField(label="Foto:", required=False)