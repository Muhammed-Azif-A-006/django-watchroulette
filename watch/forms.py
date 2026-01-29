from django import forms
from .models import WatchItem

class WatchItemForm(forms.ModelForm):

	def __init__(self, *args, user=None, **kwargs):
	        super().__init__(*args, **kwargs)
        	self.user = user

	class Meta:
		model = WatchItem
		fields = ["title", "item_type", "genre", "notes"]

	def clean_title(self):
		title = self.cleaned_data.get("title","")

		if not title or not title.strip():
			raise forms.ValidationError("Title cannot be empty.")

		if len(title.strip()) < 3:
			raise forms.ValidationError("Title must be atleast 3 characters")

		return title.strip()

	def clean(self):
		cleaned_data = super().clean()
		title = cleaned_data.get("title")

		if title and self.user:
			qs =  WatchItem.objects.filter( title__iexact = title , added_by = self.user)

			if self.instance and self.instance.pk:
				qs = qs.exclude(pk = self.instance.pk)

			if qs.exists():
				raise forms.ValidationError("You already added this item to your watchlist.")

		return cleaned_data
