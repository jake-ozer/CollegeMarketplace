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


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_permissions(self):
        # User must be authenticated if performing any action other than create/retrieve/list
        self.permission_classes = (
            [AllowAny]
            if (self.action in ["create", "list", "retrieve"])
            else [IsAuthenticated]
        )
        return super().get_permissions()

    def perform_create(self, serializer):
        if serializer.is_valid():
            validated_data = serializer.validated_data
            db_query.create_user(validated_data)


# Listing controller/handler
class ListingViewSet(viewsets.ModelViewSet):
    serializer_class = ListingSerializer

    def get_permissions(self):
        # User must be authenticated if performing any action other than retrieve/list
        self.permission_classes = (
            [AllowAny] if (self.action in ["list", "retrieve"]) else [IsAuthenticated]
        )
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
