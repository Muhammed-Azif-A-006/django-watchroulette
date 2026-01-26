from django.db import models
from django.contrib.auth.models import User

class WatchItem(models.Model):
	TYPE_CHOICES = [("MOVIE","Movie"),("ANIME","Anime"), ("SERIES","Series")]
	title = models.CharField(max_length = 150)
	item_type = models.CharField(max_length = 10, choices = TYPE_CHOICES, default = "MOVIE")
	genre = models.CharField(max_length = 50 , blank = True)
	notes = models.TextField(max_length = 100 , blank = True)
	added_by = models.ForeignKey(User,on_delete = models.CASCADE, related_name = "watch_items")
	watched = models.BooleanField(default = False)
	rating = models.IntegerField(null = True, blank = True)
	created_at = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return f"{self.title} ({self.item_type})"
