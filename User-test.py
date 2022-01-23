import unittest # Importing the unittest module
from User import User # Importing the User class
class TestUser(unittest.TestCase):
    '''
    Test class that defines test case for the User class behaviour.
    
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_User = User("Lilian","Kanana","kenjwdn34@b","liliankanana.com") # create User object
        
        def test_init(self):
            '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_User.first_name,"Lilian")
        self.assertEqual(self.new_User.last_name,"Kanana")
        self.assertEqual(self.new_User.password,"kenjwdn34@b")
        self.assertEqual(self.new_User.email,"liliankanana.com")
        
        def test_save_User(self):
            '''
        test_save_User test case to test if the user object is saved into
         the  users list
        '''
        self.new_User.save_User() # saving the new User
        self.assertEqual(len(User.listOfUser),1)

