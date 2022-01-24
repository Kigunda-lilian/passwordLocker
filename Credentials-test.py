import unittest
from Credentials import Credential

class TestCredential(unittest.TestCase):
   
    def setUp(self):
       
        self.new_credential = Credential( "Lucy", "acapulco4321") #create credential object
        
    def test_init(self):
       
        self.assertEqual(self.new_credential.profile, "Lucy")
        self.assertEqual(self.new_credential.password, "acapulco4321")
        
    def test_save_profile(self):
        
        self.new_credential.save_profile()
        self.assertEqual(len(Credential.password_list),1)
        
    def tearDown(self):
        '''
        tearDown function that does clean up after each test case has run.
        '''
        Credential.password_list = []
        
    def test_save_multiple_profile(self):
        '''
        test case to check whether we can save multiple profiles
        '''
        self.new_credential.save_profile()
        test_credential = Credential( "Faith", "Faith1234")
        test_credential.save_profile()
        
    def test_delete_profile(self):
        '''
        test case that checks if a profile can be removed.
        '''
        self.new_credential.save_profile()
        test_credential = Credential("Faith", "Faith1234")
        test_credential.save_profile()

        test_credential.delete_profile()
        self.assertEqual(len(Credential.password_list),1)
        
    def test_display_all_profile(self):
        '''
        test case to check whether we can display all user profiles.
        '''
        self.new_credential.save_profile()
        test_credential = Credential("Faith", "Faith1234")
        test_credential.save_profile()

        self.assertEqual(Credential.display_profile(), Credential.password_list)


if __name__ == '__main__':
    unittest.main()