from django import forms

class WordsForm(forms.Form):
    count = forms.IntegerField()
    camelcase = forms.BooleanField(required=False)
