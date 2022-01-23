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
        
        # tearDown() method helps us get accurate test results every time a new test case.
        
        def tearDown(self):
            '''
        tearDown function that does clean up after each test case has run.
        '''
        User.listOfUser = []
        
        # test if we can save multiple users in our  listlistOfUser.
        
        def test_save_multiple_User(self):
            '''
        test_save_multiple_User to check if we can save multiple User
            objects to our listOfUser
        '''
        self.new_User.save_User()
        test_User = User("Elijah", "Mutie", "acapulco#26","ellytie@gmail.com")
        test_User.save_User()
        self.assertEqual(len(User.listOfUser), 2)

#feature to delete Users

def test_delete_User(self):
        '''
        to test if we can remove a user from our user list.
        '''
        self.new_user.save_User()
        test_User = User("Elijah", "Mutie", "acapulco#26","ellytie@gmail.com")
        test_User.save_User()

        self.new_User.delete_User() #deleting a user object
        self.assertEqual(len(User.listOfUser), 1)
        
        
        def test_find_User_by_first_name(self):
            '''
        to  find a user by their first_name
        '''
        self.new_User.save_User()
        test_User = User("Elijah", "Mutie", "acapulco#26","ellytie@gmail.com")
        test_User.save_User()

        found_User = User.find_by_first_name("Elijah")
        self.assertEqual(found_User.first_name, test_User.first_name)
        
        
        def test_User_exists(self):
            '''
        test to  return a boolean if the account exists or not.
        '''
        self.new_User.save_User()
        test_User = User("Elijah", "Mutie", "acapulco#26","ellytie@gmail.com")
        test_User.save_User()

        User_exists = User.User_exists("Elijah")
        self.assertTrue(User_exists)
        
        
        def test_display_all_Users(self):
            '''
        method that returns a list of all users saved.
        '''
        self.assertEqual(User.display_Users(), User.listOfUser)