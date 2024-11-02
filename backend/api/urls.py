from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, ListingViewSet

# Alternatively we can do
"""
listing_list = ListingViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
listing_detail = ListingViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
with urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('listings/', listing_list, name='listing-list'),
    path('listings/<int:pk>/', listing_detail, name='listing-detail'),
"""

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"listings", ListingViewSet, basename="listing")
""" The router creates the following urlpatterns:
- listings/,  name='listing-list'
- listings/<int:pk>/, name='listing-detail'
- users/,  name='user-list'
- users/<int:pk>/, name='user-detail'
"""


urlpatterns = [
    path('', include(router.urls)),
]
