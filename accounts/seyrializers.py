from rest_sramework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = '__all__'
