#user_handler.py (created by CHASE)
from django.contrib.auth.hashers import check_password
from .models import User 

class UserHandler:
    def __init__(self, user):
        self.user = user
    
    #login function
    def login(self, username, password):
        #Implement login logic here. EDIT as this is basic
        if self.user.username == username and check_password(password, self.user.password):
            return True
        else:
            return False
        
    #logout function
    def logout(self):
        #Implement logout logic here (e.g., clear session or tokens) EDIT LATER
        pass

    #update_account function
    def update_account(self, username, password):
        #Add logic later 
        pass
