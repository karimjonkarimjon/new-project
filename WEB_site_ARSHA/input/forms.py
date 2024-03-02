from django import forms
from .models import Input

class InpForm(forms.ModelForm):
    class Meta:
        model = Input
        fields = ["inp"]
    def __init__(self, *args, **kwargs):
        super(InpForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({"class":"form-control"})