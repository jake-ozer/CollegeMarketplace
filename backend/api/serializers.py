from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers
from .models import Listing, User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)  # Wont be revealed in reads

    def create(self, validated_data):
        hashed_password = make_password(validated_data["password"])  # Hash the password
        return User(
            id=None,
            username=validated_data["username"],
            password=hashed_password,  # Store the hashed password
        )


class ListingSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=500)
    created_at = serializers.DateTimeField(read_only=True)
    # maybe change write_only for author_id
    author_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        """
        Create and return a new Listing instance, given the validated data.
        """
        return Listing(
            id=None,  # ID will be auto-incremented in SQL
            title=validated_data["title"],
            description=validated_data["description"],
            created_at=None,  # Time will be set in SQL
            author_id=validated_data["author_id"],
        )

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        return instance

    def validate(self, attrs):
        if not attrs.get("title"):
            raise serializers.ValidationError("Title is required.")
        if not attrs.get("description"):
            raise serializers.ValidationError("Description is required.")
        return attrs
