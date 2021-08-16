from django import forms
from django.db.models import fields
from .models import Dept

class DeptModelForm(forms.ModelForm):
    class Meta:
        model = Dept
        fields = '__all__'

    def clean_intake(self):
        user_entered_intake = self.cleaned_data['intake']
        if user_entered_intake<30:
            raise forms.ValidationError('You need at least 30 seats to start department...')
        else:
            return user_entered_intake