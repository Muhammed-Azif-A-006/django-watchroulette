from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_list_api(request):
	profiles = Profile.objects.all()
	serializer = ProfileSerializer(profiles,many = True)
	return Response(serializer.data)

@api_view(['GET'])
def hello_api(request):
    return Response({
        "message": "Hello from API",
        "user": str(request.user)
    })
