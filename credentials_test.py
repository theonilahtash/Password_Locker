import unittest # Importing the unittest module
# import pyperclip
from credentials import Credentials # Importing the credential class       
import user

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

    def test_save_credential(self): 
        '''
        test_save_credential test case to test if the credential object is saved into the credential list
        ''' 
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(Credentials.credential_list),1) 

    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple credential objects to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Test","user","0733445566","test@user.com","password") # new credential
        test_credential.save_credential()
        self.assertEqual(len(Credentials.credential_list),2)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credential_list = []

 # other test cases here
    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple credential objects to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("Test","user","0733445566","test@user.com") # new credential
        self.assertEqual(len(Credentials.credential_list),1)

    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential from our credential list
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("Test","user","0733445566","test@user.com") # new credential
        test_credential.save_credential()

        self.new_credential.delete_credential() # Deleting a credential object
        self.assertEqual(len(Credentials.credential_list),1)

    def test_find_credential_by_user_name(self):
        '''
        this will check if we can find a credential by user name and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credentials("b_belvo", "0722334455", "b_belvo@gmail.com", "password")
        test_credential.save_credential()

        found_credential = Credentials.find_by_user_name("b_belvo")
        self.assertEqual(found_credential.user_name, test_credential.user_name) 

    def test_credential_exist(self):
        '''
        check if credentials exist and return a boolean
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("b_belvo", "0722334455", "b_belvo@gmail.com", "password") 

        credentials_exist = Credentials.credential_exist    
        self.assertTrue(credentials_exist) 

    def test_display_all_credentials(self):
        '''
        test method that returns a list of all the credentials saved.
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("theonilahtash", "0733445566", "theonilahtash@gmail.com", "tash1234") 
        test_credential.save_credential()
        # self.assertEqual(credentials.display_credentials(), Credentials.credential_list)

    # def test_copy_user_name(self):
    #     '''
    #     Test to confirm that we are copying user name credentials found
    #     '''

    #     self.new_credentials.save_credentials()
    #     Credentials.copy_username("theonilahtash")

    #     self.assertEqual(self.new_credentials.user_name, pyperclip.paste()) 
# class TestUser(unittest.TestCase):
#     def setUp(self):
#         '''
#         method run before each test case
#         '''
#         self.new_user = user("theonilahtash", "password")


#     def tearDown(self):
#         '''
#         Method to give an empty array before each test for more accurate results
#         '''
#         User.user_list = []

#     def test_user_init(self):
#         '''
#         method to test if our users are being instantiated correctly
#         '''
#         self.assertEqual(self.new_user.login_name, "theonilahtash")
#         self.assertEqual(self.new_user.password, "password")



#     def test_save_user(self):
#         '''
#         Method to test if users are being saved
#         '''
#         self.new_user.save_user()
#         self.assertEqual(len(user.user_list), 1)


#     def test_save_multiple_user(self):
#         '''
#         Method to test if multiple users ate being saved
#         '''
#         self.new_user.save_user()
#         test_user = user("Winnie34", "password")
#         test_user.save_user()

#         self.assertEqual(len(user.user_list), 2)

#     def test_login(self):
#         '''
#         method to test login credentials
#         '''
#         self.new_user.save_user()
#         test_user = user("theonilahtash", "password")
#         test_user.save_user()

#         login_credentials = user.user_login("theonilahtash")
#         self.assertEqual(login_credentials.login_name, test_user.login_name)





if __name__ == '__main__':
    unittest.main()      

