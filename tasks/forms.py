

from .models import Variant

from django.forms import ModelForm


class VariantForm(ModelForm):




    class Meta:
        model = Variant
        fields = ['variant']

