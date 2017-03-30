from django.forms import ModelForm
from .models import Request, Stakeholder

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ['title', 'date_created', 'date_requested',
                      'stakeholder', 'analysts', 'databases']

class StakeholderForm(ModelForm):
    class Meta:
        model = Stakeholder
        fields = ['name', 'title', 'department', 'email', 'phone_number']

