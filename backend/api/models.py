'''
CONTAINS:
-Classes: User, Message, SMS Message, Listing

'''

# Create your models here. Models are essentially DB tables
'''
CLASS: User
'''
class User(AbstractUser):
    #Functions
    def __init__(self, id, username, password=None):
        self.id = id
        self.username = username
        self.password = password  # Store hashed password directly
        
    def __str__(self):
        return self.username   
    
    def check_password(self, password):
        return check_password(password, self.password) 
    

'''
CLASS: Message
'''
class Message:
    message_text = models.TextField()

    #Functions
    def __init__(self, id):
        self.id = id
 
'''
SUB-CLASS: SMS Message
'''
class SMSMessage(Message):
    # SMS-specific fields
    # Functions        
    def __init__(self, id):
        self.id = id

'''
CLASS: Listing
'''
class Listing:
    def __init__(self, id, title, description, created_at, author_id):
        self.id = id
        self.title = title
        self.description = description
        self.created_at = created_at
        self.author_id = author_id

    def __str__(self):
        return self.title
    


