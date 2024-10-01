from django.db import models
from django.contrib.auth.models import User


# Create your models here. Models are essentially DB tables
class Listing(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # on_delete=models.CASCADE means all the users posts will be deleted when the user is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")

    def __str__(self):
        return self.title
    
class ListingItem(models.Model):
    # on_delete=models.CASCADE means all the users posts will be deleted when the user is deleted
    listing = models.OneToOneField(Listing, on_delete=models.CASCADE, primary_key=True,)
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name