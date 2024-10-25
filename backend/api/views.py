from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from backend.db_utils.queries import SQLiteDBQuery
from backend.db_utils.db_factory import db_configs, DBType
from .serializers import UserSerializer, ListingSerializer
from .models import Listing

# Initialize specific query object
db_query = SQLiteDBQuery(db_configs[DBType.SQLITE])


# Create your views here.
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        # Custom database logic for user creation
        if serializer.is_valid():
            # Save user to the database using your custom logic
            print("will create new user")
            # create_user(serializer.validated_data)
        else:
            print(serializer.errors)


class ListingViewSet(viewsets.ModelViewSet):
    serializer_class = ListingSerializer

    def get_permissions(self):
        # User must be authenticated if creating or destroying listing
        self.permission_classes = [IsAuthenticated] if (self.action in ["create", "destroy"]) else [AllowAny]
        return super().get_permissions()

    def get_queryset(self):
        listings = db_query.get_all_listings()
        return [Listing(**listing) for listing in listings]

    def perform_create(self, serializer):
        data = serializer.validated_data
        user_id = self.request.user.id
        db_query.create_listing(data, user_id)

    def perform_destroy(self, instance):
        db_query.delete_listing(instance.id)
