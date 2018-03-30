from django import forms
from django.forms import ModelForm

class TextForm(forms.Form):
	#province = forms.CharField()
	price = forms.CharField(required=False)


PROVINCE_CHOICE = (
    ('AB','Alberta'),
    ('BC','British Columbia'),
    ('MB','Manitoba'),
    ('NB','New brunswick'),
    ('NL','Newfoundland and Labrador'),
    ('NS','Nova Scotia'),
    ('NT','Northwest Territories'),
    ('ON','Ontario'),
    ('PE','PEI'),
    ('QC','Quebec'),
    ('SK','Saskatchewan'),
    ('YT','Yukon'),
)


class DropdownForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(DropdownForm, self).__init__(*args, **kwargs)
        self.fields['province'] = forms.ChoiceField(choices=PROVINCE_CHOICE,required=False)