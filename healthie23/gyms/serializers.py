from rest_framework import serializers
from gyms.models import Gym


class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = ('id', 'owner', 'name')
        owner = serializers.ReadOnlyField(source='owner.username')
