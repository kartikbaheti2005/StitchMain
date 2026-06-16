from django.forms import forms
from .models import UpperBody, LowerBody

SHIRT_FIELDS = ['shoulder', 'chest', 'waist', 'sleeve', 'collar', 'button_type']
COAT_FIELDS = ['shoulder', 'chest', 'waist', 'sleeve', 'length']
PANT_FIELDS = ['waist', 'hips', 'thigh', 'inseam', 'bottom_width', 'length']
PLAZO_FIELDS = ['waist', 'hips', 'length', 'bottom_width']

CLOTH_FIELDS_MAP = {
    'shirt': SHIRT_FIELDS,
    'coat': COAT_FIELDS,
    'pant': PANT_FIELDS,
    'plazo': PLAZO_FIELDS,
    # add new cloth type here in future — no new model needed!
}

class UpperBodyMeasurementForm(forms.ModelForm):
    class Meta:
        model = UpperBody
        fields = '__all__'

    def __init__(self, cloth_type, *args, **kwargs):
        super().__init__(*args, **kwargs)
        allowed = CLOTH_FIELDS_MAP.get(cloth_type, [])
        # Remove fields not needed for this cloth type
        for field in list(self.fields):
            if field not in allowed and field != 'cloth_type':
                del self.fields[field]


class LowerBodyMeasurementForm(forms.ModelForm):
    class Meta:
        model = LowerBody
        fields = '__all__'

    def __init__(self, cloth_type, *args, **kwargs):
        super().__init__(*args, **kwargs)
        allowed = CLOTH_FIELDS_MAP.get(cloth_type, [])
        # Remove fields not needed for this cloth type
        for field in list(self.fields):
            if field not in allowed and field != 'cloth_type':
                del self.fields[field]