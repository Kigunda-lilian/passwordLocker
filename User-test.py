import unittest # Importing the unittest module
from User import User # Importing the User class
class TestUser(unittest.TestCase):
    '''
    Test class that defines test case for the User class behaviour.
    
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    # test if our objects are being instantiated correctly.
    
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
        
        # test if our users are being saved.
        
        def test_save_User(self):
            '''
        test_save_User test case to test if the user object is saved into
         the  users list
        '''
        self.new_User.save_User() # saving the new User
        self.assertEqual(len(User.listOfUser),1)
        
        def test_save_multiple_User(self):
            '''
        test_save_multiple_User to check if we can save multiple User
            objects to our listOfUser
        '''
        self.new_User.save_User()
        test_User = User("Elijah", "Mutie", "acapulco#26","ellytie@gmail.com")
        test_User.save_User()
        self.assertEqual(len(User.listOfUsert), 2)

