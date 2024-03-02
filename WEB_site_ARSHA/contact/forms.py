from django import forms
from .models import contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ["your_name", "your_email", "your_msg"]
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({"class":"form-control"})