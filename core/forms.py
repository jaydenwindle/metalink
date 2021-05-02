from django import forms

from core.models import Link

class LinkForm(forms.ModelForm):

    class Meta:
        model = Link
        fields = ("url", "title", 'description', 'image')
