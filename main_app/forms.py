from django import forms
from django.forms import ModelForm
from main_app.models import MyModel

class TextForm(forms.Form):
	#province = forms.CharField()
	price = forms.CharField()


class DropdownForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['province']