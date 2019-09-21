from django import forms
from django.forms import widgets


class VisitorForm(forms.Form):
    author = forms.CharField(max_length=40, label='Author', required=True)
    email = forms.EmailField(max_length=50, label='Email', required=True)
    text = forms.CharField(max_length=3000, label='Text', required=True,
                           widget=widgets.Textarea)
