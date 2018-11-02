class Credentials:
    """
    Class that generates new instances of credentials
    """

    credential_list = [] # empty credential list

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