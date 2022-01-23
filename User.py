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
        
def save_User(self):
            '''
            function to add a new user to the  listofUser array
            '''
            User.listOfUser.append(self)  
            
def delete_User(self):
        '''
        method deletes a saved user from the user list.
        '''

        User.listOfUser.remove(self)
        
        
        @classmethod
        def find_by_first_name(cls, first_name):
          '''
        method that takes in a name and returns a firstname that matches that name.
        Args:
            firstname:name to search for
        Returns:
            username of person that matches the firstname.
        '''
        for User in cls.listOfUser:
            if User.first_name == first_name :
                return User
            
            
        @classmethod
        def User_exists(cls,  first_name):
         '''
        method that checks if a user exists from the user list.
        Args:
            first_name: first_name to search the account exists.
        Returns:
            Boolean: true or false depending if the user exists.
        '''
        for User in cls.listOfUser:
            if User.first_name == first_name:
                return True

        return False
    
        @classmethod
        def display_Users(cls):
         '''
        method that returns the user list
        '''
        return cls.listOfUser
        
        