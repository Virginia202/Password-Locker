import string
import random

class Credentials:
    '''
    class that generates new instance of credentials
    '''
    credentials_list = []
def __init__(self, user_name,acc_name,email,acc_password,):
    '''
    defining the object properties
    '''    

    self.user_name = user_name
    self.acc_name = acc_name    
    self.acc_password = acc_password
    self.email = email

def save_credentials(self):
    '''
    this method will save infomation of the user
    '''
    Credentials.credential_list.append(self)

def delete_credentials(self):
    '''

    delete_contact method deletes a saved contact from the users_list

    '''
    Credentials.credentials_list.remove(self)


def random_password(self):
    '''method to generate a random password'''

    characters = string.ascii_lowercase + string.digits
    gen_password = ''.join(random.choice(characters) for i in range (0,12))

    return gen_password

@classmethod
def find_by_number(cls,number):
    '''
    Method that takes in a number and return a user that matches that number.
    '''
        
    for credentials in cls.credentials_list:
            if credentials.number == number:
                return credentials

def credentials_exist(cls,number):
    for credentials in cls.credentials_list:
            if credentials.number == number:
                return credentials
                
                return True    

@classmethod
def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.user_list                                        