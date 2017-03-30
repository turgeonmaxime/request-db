from django.forms import ModelForm
from .models import Request

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ['title', 'date_created', 'date_requested',
                      'stakeholder', 'analysts', 'databases']

