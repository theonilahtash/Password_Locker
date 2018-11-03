# import pyperclip
import random

class Credentials:
    """
    Class that generates new instances of credentials
    """

    credential_list = [] # empty credential list
 # Init method here
    def save_credential(self):
        '''
        save_credential method saves credential objects into credential_list
        '''

        Credentials.credential_list.append(self)

    def __init__(self,user_name,phone_number,email,password):

        """
        user_name: New credential username.
        number: New credential phone number. 
        email: New credential email adress.
        password: New credential password.
        """

        self.user_name = user_name
        self.phone_number = phone_number
        self.email = email
        self.password = password

    def delete_credential(self):
        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credentials.credential_list.remove(self)

    @classmethod
    def find_by_user_name(cls, name):
        '''
        This is a method that in which user can find credentials by name search
        '''
        for credentials in cls.credential_list:
            if credentials.user_name == name:
                return credentials

    @classmethod
    def credential_exist(cls,name):
        '''
        method that checks if the credentials ade are already on the credential_list and return true (if exists) and false(if does not)
        '''
        for credentials in cls.credential_list:
            if credential.user_name == name:
                return True

        return false 
    
    @classmethod
    def credential_display(cls,name):
        '''
        method that checks if the credentials  already display on the  credential_list and return true (if exists) and false(if does not)
        '''
        for credentials in cls.credential_list:
            if credential.user_name == name:
                return True

        return false 
            

    