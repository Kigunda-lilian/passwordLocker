class Credential:
    
    password_list = []

    def __init__(self, profile, password):
        '''
        function helps us define properties of our objects
        '''
        self.profile = profile
        self.password = password
        
    def save_profile(self):
        
        Credential.password_list.append(self)

    def delete_profile(self):
        
        Credential.password_list.remove(self)
        
    @classmethod
    def display_profile(cls):
       
        return cls.password_list
    
    
 