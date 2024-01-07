from django import forms
from django.core import validators
# def starts_with_m(value):
#     if value[0].lower()!='d':
#         raise forms.ValidationError('name starts with d')

class studentform(forms.Form):
    name = forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(15),validators.MinLengthValidator(5)])
    # rno = forms.IntegerField()
    # name = forms.CharField(validators=[starts_with_m])

    # def clean_name(self):
    #     print("name field validation")
    #     inputname = self.cleaned_data['name']
    #     if len(inputname) > 4:
    #         raise forms.ValidationError('the minimum length should be more')
    #     return inputname
    # name = forms.CharField()
    # def clean(self):
    #     total_data = super().clean()
    #     inputname = total_data['name']
    #     if inputname[0].lower != 's':
    #         raise forms.ValidationError('the name should be starts with s')
    #     return inputname