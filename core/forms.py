from django import forms

from core.models import Link

class LinkForm(forms.ModelForm):

    class Meta:
        model = Link
        fields = ("url", "title", 'description', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['url'].widget.attrs['placeholder'] = "https://yoursite.com"
        self.fields['title'].widget.attrs['placeholder'] = "This link is really cool"
        self.fields['description'].widget.attrs['placeholder'] = "An informative description of the link"
