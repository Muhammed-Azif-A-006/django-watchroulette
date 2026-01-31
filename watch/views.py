from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
import random
from .models import WatchItem
from .forms import WatchItemForm
from django.contrib import messages
@login_required
def dashboard(request):
	items = WatchItem.objects.select_related("added_by").filter(added_by = request.user).order_by("-created_at")
	unwatched = items.filter(watched = False)

	pick = None

	if request.GET.get("spin") == "1" and unwatched.exists():
		pick = random.choice(list(unwatched))

	return render(request, "watch/dashboard.html",{"items" : items, "unwatched_count" : unwatched.count(), "pick" : pick})

@login_required
def add_item(request):
	if request.method == "POST":
		form = WatchItemForm(request.POST, user = request.user)
		if form.is_valid():
			item = form.save(commit=False)
			item.added_by = request.user
			item.save()

			messages.success(request,"Item added to your watch list ..")
			return redirect("watch-dashboard")

	else:
		form = WatchItemForm(user = request.user)

	return render(request, "watch/add_item.html", {"form": form})

@login_required
def mark_watched(request, item_id):
	item = get_object_or_404(WatchItem, id=item_id, added_by=request.user)
	item.watched = True
	item.save()
	messages.success(request, "Marked as watched ✅")
	return redirect("watch-dashboard")

@login_required
def rate_item(request, item_id):
	item = get_object_or_404(WatchItem, id=item_id, added_by=request.user)

	if request.method == "POST":
		try:
			rating = int(request.POST.get("rating"))
		except (TypeError, ValueError):
			rating = None

		if rating is not None and 1 <= rating <= 10:
			item.rating = rating
			item.save()
			messages.success(request, "Rating saved ⭐")
			return redirect("watch-dashboard")


		return render(request, "watch/rate_item.html", {
			"item": item,
			"error": "Rating must be a number between 1 and 10."
		})

	return render(request, "watch/rate_item.html", {"item": item})
