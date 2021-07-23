from django import forms
from django.db.models import fields
from django.forms.models import ALL_FIELDS
from .models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields='__all__'
        labels={'photo':''}