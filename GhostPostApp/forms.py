from django import forms
from .models import Posts

class AddPostForm(forms.Form):

    BOOL_CHOICES = ((True, 'Roast'), (False, 'Boast'))

    post = forms.CharField(widget=forms.Textarea, max_length=280, initial='Your Post')
    boast_or_roast = forms.ChoiceField(choices = BOOL_CHOICES, label="Boast Or Roast", 
                              initial='', widget=forms.Select(), required=True)

