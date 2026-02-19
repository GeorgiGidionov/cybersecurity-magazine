from django import forms
from .models import Subscription
from datetime import date

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['plan', 'subscriber_name', 'subscriber_email', 'start_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'plan': 'План',
            'subscriber_name': 'Име и фамилия',
            'subscriber_email': 'Имейл',
            'start_date': 'Начална дата',
        }
        help_texts = {
            'start_date': 'Моля, изберете дата в бъдещето.',
        }

    def clean_start_date(self):
        start = self.cleaned_data.get('start_date')
        if start < date.today():
            raise forms.ValidationError('Началната дата не може да бъде в миналото.')
        return start