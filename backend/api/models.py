from django.contrib.auth.hashers import check_password

# Create your models here. Models are essentially DB tables
class User:
    def __init__(self, id, username, password=None):
        self.id = id
        self.username = username
        self.password = password  # Store hashed password directly
        
    def __str__(self):
        return self.username   
    
    def check_password(self, password):
        return check_password(password, self.password) 
    

class Listing:
    def __init__(self, id, title, description, created_at, author_id):
        self.id = id
        self.title = title
        self.description = description
        self.created_at = created_at
        self.author_id = author_id

    def __str__(self):
        return self.title

