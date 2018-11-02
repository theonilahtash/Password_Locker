import unittest # Importing the unittest module
from credentials import Credentials # Importing the credential class
#import pyperclip
#from user import User

class TestCredential(unittest.TestCase):

    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''    

    def setUp(self):
        '''
        set up method to run before each test cases.
        '''
        self.new_credential = Credentials("theonilahtash","0733445566","theonilahtash@gmail.com","tash1234") # create credential object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.user_name,"theonilahtash")
        self.assertEqual(self.new_credential.phone_number,"0733445566") 
        self.assertEqual(self.new_credential.email,"theonilahtash@gmail.com")
        self.assertEqual(self.new_credential.password,"tash1234")

    def test_save_credential(self)  
        '''
        test_save_credential test case to test if the credential object is saved into the credential list
        ''' 
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(Credentials.credential_list),1)     


if __name__ == '__main__':
    unittest.main()      

