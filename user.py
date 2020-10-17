class User:
    '''
    Class that generates new instances of users    
    
    '''
    user_list = []
def __init__(self, username,number,email,password):
    '''
    defining the object properties
    '''    

    self.username = username
    self.number = number
    self.password = password
    self.email = email



@classmethod
def display_users(cls):
    '''
    method display users
    '''
    return cls.user_list

def delete_user(self):
    '''
    delete_contact method deletes a saved contact from the users_list

    '''
    User.user_list.remove(self)


@classmethod
def find_by_number(cls,number):
    '''
    Method that takes in a number and return a user that matches that number.
    '''
        
    for user in cls.user_list:
            if user.number == number:
                return user


@classmethod
def user_exist(cls,number):
    '''
    Method that checks if a user exists from the user list.
    Args:
    number: Phone number to search if it exists
    Returns :
    Boolean: True or false depending if the user exists
    '''
    for user in cls.user_list:
        if user.number == number:

                return True
                return False