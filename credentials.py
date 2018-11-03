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
    def find_by_user_name(cls,name):
        '''
        method that takes in a name and returns a credential that matches that name.

        Args:
            name: user name to search for 
        returns:
            Credentials of a person that matches the name.
        '''

    for credential in cls.credential_list:
        if credential.user_name == name:
            return credential 

    