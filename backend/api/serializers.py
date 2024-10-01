from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Listing,ListingItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        # password is write only - cant read it when requested
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ["id", "title", "description", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}

class ListingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingItem
        fields = ["listing", "name", "description", "created_at"]
        #extra_kwargs = {"parentListing": {"read_only": True}}