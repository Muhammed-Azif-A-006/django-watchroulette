from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import WatchItem
from .serializers import WatchItemSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])

def watch_list_api(request):
	items = WatchItem.objects.select_related("added_by").filter(added_by = request.user)
	serializer = WatchItemSerializer(items,many = True)
	return Response(serializer.data)
