
from user import User
from credentials import Credentials


def user_name(uname, password):
    '''
    Function to create new account
    '''
    new_user = User(uname, password)
    return new_user


def save_new_user(user):
    '''
    Function to save a user
    '''
    user.save_user()


def account_login(login):
    '''
    Function to login
    '''
    return User.user_login(login)


def create_credentials(user_name,phone_number,email,password):
    '''
    Function to create new credentials
    '''
    new_credentials = Credentials(user_name,phone_number,email,password)
    return new_credentials


def save_user_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()


def del_credentials(credentials):
    '''
    Function to delete credentials from list
    '''
    credentials.delete_credentials()


def find_credentials(name):
    '''
    Function that finds a credentials by user name and return details
    '''
    return Credentials.find_by_user_name(name)


def copy_username(name):
    return Credentials.copy_username(name)


def check_credentials_exist(name):
    '''
    Function to check if a credentials exists
    '''
    return Credentials.credentials_exist(name)


def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.credential_display()


def main():
    print("Theonilah password locker Welcome!!")
    while True:
        print('''
              crt - create account
              log - login
              esc - Escape''')
        short_code = input().lower()
        print("_" * 20)
        if short_code == "crt":
            print("Create Acount")
            print("Kindly Create a username")
            print("_" * 20)
            uname = input()
            print("Choose a password")
            password = input()
            print("_" * 20)
            save_new_user(User(uname, password))
            print(f"""Your user details - Username : {uname} Password : {password}""")
            print("")
            print(f"Hello {uname} please choose from the options below")
            print("")

            while True:
                print("Use these short codes: cc - create new credentials, dc - display credentials,  wq - exit credentials list")
                short_code = input().lower()

                if short_code == 'cc':
                        print("New credentials")
                        print("-"*10)

                        print('')

                        print("User name ...")
                        u_name = input()

                        print('')

                        print("Phone number ...")
                        phone_number = input()

                        print('')

                        print("Email address ...")
                        email = input()

                        print('')

                        print("Account password")
                        acc_password = input()

                        save_user_credentials(create_credentials(u_name, phone_number, email, acc_password))
                        print('')

                        print(f"New credential username : {u_name}, Phone number: {phone_number}")
                        print('')
                elif short_code == 'dc':
                        if display_credentials():
                            print("This is a list of all the credentials")
                            print('')
                            for Credentials in display_credentials():
                                print(f"Username : {Credentials.user_name}, Phone number : {Credentials.phone_number} E-mail address : {Credentials.email} Password : {Credentials.password}")

                                print('')
                        else:
                            print('')
                            print("oops sorry, you have not  saved any credentials")
                            print('')
                elif short_code == "wq":
                        print('')
                        print("Goodbye ...")
                        break
                else:
                    print("input a valid  code")

        elif short_code == "log":
            print("Log in")
            print("please enter a user Name")
            print("_" * 20)
            uname = input()
            print("Enter your password")
            print("_" * 20)

            print(f"Hello {uname} please can you choose from the options below")
            print("")
            while True:
                print("Use these short codes: cc - create new credentials, dc - display credentials, wq - exit credentials list")
                short_code = input().lower()

                if short_code == 'cc':
                        print("New credentials")
                        print("-"*10)

                        print('')

                        print("User name ...")
                        u_name = input()

                        print('')

                        print("Phone number ...")
                        phone_number = input()

                        print('')

                        print("Email address ...")
                        email = input()

                        print('')

                        print("Account password")
                        acc_password = input()

                        save_user_credentials(create_credentials(u_name, phone_number, email, acc_password))
                        print('')

                        print(f"New credential account : {u_name}, User name : {phone_number}")
                        print('')
                elif short_code == 'dc':
                        if display_credentials():
                            print("Here is a list of all the credentials")
                            print('')
                            for Credentials in display_credentials():
                                print(f"Username : {Credentials.user_name}, Phone number : {Credentials.phone_number} E-mail address : {Credentials.email} Password : {Credentials.password}")

                                print('')
                        else:
                            print('')
                            print("oops sorry, you have not saved any credentials")          
                elif short_code == "wq":
                        print('')
                        print("Goodbye ...")
                        break
                else:
                    print("Enter a valid  code")

        elif short_code == "esc":
            print('')
            print("Exiting Bye Bye from Theo")
            break
        else:
            print("oops sorry, the short code does not  exist")


if __name__ == '__main__':
    main()