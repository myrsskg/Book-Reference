# -*- coding: utf-8 -*-
from django import forms
from .models import BR


class FormBR(forms.ModelForm):
    class Meta:
        fields='__all__'
        model = BR
