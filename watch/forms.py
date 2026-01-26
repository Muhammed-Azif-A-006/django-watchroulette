from django import forms
from .models import WatchItem

class WatchItemForm(forms.ModelForm):
	class Meta:
		model = WatchItem
		fields = ["title", "item_type", "genre", "notes"]
