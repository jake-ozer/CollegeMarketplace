from django.db import models
from django.contrib.auth.models import User


# Create your models here. Models are essentially DB tables
class Listing:
    def __init__(self, id, title, description, created_at, author_id):
        self.id = id
        self.title = title
        self.description = description
        self.created_at = created_at
        self.author_id = author_id

    def __str__(self):
        return self.title

