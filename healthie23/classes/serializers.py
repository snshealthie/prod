from rest_framework import serializers
from classes import models


class ClassesSerializer(serializers.ModelSerializer):
    reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # reviews2 = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='apiv2:review-detail')
    #  hyperlinked approach
    # reviews3 = review_serializer.ReviewSerializer(many=True, read_only=True) send everything nested (not good)

    class Meta:
        model = models.Classes
        fields = ('id', 'owner', 'name', 'gym', 'reviews')
        owner = serializers.ReadOnlyField(source='owner.username')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {'owner': {'write_only':True}}
        # email has to come in, get written (supplied by the user), but does not get written we we send back
        model = models.Review
        fields = ('id', 'review', 'rating', 'owner')
        owner = serializers.ReadOnlyField(source='owner.username')