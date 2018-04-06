from mpmath import isint

from .models import Variant
import django.forms as forms
from django.forms import ModelForm
import django.core.validators as validators

class VariantForm(ModelForm):




    class Meta:
        model = Variant
        fields = ['variant']

