from django import forms
from .models import feedback

class feedback_form(forms.ModelForm):

    class Meta:
        model = feedback
        fields = ('name','email','feedback')
        widgets ={'name': forms.TextInput(attrs={'placeholder': 'Your name',
                                                 'class':'form-control form-control-sm styled-input'}),
                  'email': forms.TextInput(attrs={'placeholder': 'Your email',
                                                 'class':'form-control form-control-sm styled-input'}),
                  'feedback': forms.TextInput(attrs={'placeholder': 'Your feedback',
                                                 'class':'form-control form-control-sm styled-input'})}

 

