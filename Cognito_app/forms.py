from django import forms
import re

class CognitoAuthForm(forms.Form):
    email = forms.EmailField(required=True,
                            error_messages = {
                            'required': 'Email required.'
                            })
    # password = forms.CharField(
    #                         required=True,
    #                         min_length=8,
    #                         error_messages = {
    #                             'required':'Password Required.',
    #                             'min_length':'Minimum length should not be less than 8 characters.'
    #                         })

