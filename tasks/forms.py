

from .models import variant

from django.forms import ModelForm


class VariantForm(ModelForm):




    class Meta:
        model = variant
        fields = ['variant']

