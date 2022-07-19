from django.forms import ModelForm
from .models import Feeding, Use

class FeedingForm(ModelForm):
  class Meta:
    model = Feeding
    fields = ['date', 'meal']

class UseForm(ModelForm):
  class Meta:
    model = Use
    fields = ['use', 'rating']