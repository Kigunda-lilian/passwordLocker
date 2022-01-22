class User:
    """
    Class that generates new instances of User
    """
listOfUser=[]

def __init__(self,first_name,last_name,password,email):
    
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            first_name: New user first name.
            last_name : New user last name.
            password : New user password.
            email : New user email address.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        
def save_user(self):
            '''
            function to add a new user to the  listofUser array
            '''
            User.listOfUser.append(self)  
            
