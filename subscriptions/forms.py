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
            'plan': 'Subscription Plan',
            'subscriber_name': 'Full Name',
            'subscriber_email': 'Email Address',
            'start_date': 'Start Date',
        }
        help_texts = {
            'start_date': 'Select the date you want the subscription to begin.',
        }

    def clean_start_date(self):
        start = self.cleaned_data.get('start_date')
        if start < date.today():
            raise forms.ValidationError('Start date cannot be in the past.')
        return start