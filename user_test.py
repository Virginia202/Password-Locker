import unittest # Importing the unittest module
from user import User
from Credentials import Credentials

class TestUser(unittest.TestCase):
        '''
        Test class that defines test cases for the user class behaviors


        Args:
        unittest.TestCase: TestCase class that helps in creating test cases

        ''' 

def setUp(self):

        '''
        this  Set up method is set to run before each test cases.

        '''
        self.new_user = User("Eli","0707569981","20088","elykip@gmail.com") # create user object

def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list= []  

def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_username.username,"Eli")
        self.assertEqual(self.new_number.number,"0707569981")
        self.assertEqual(self.new_.email,"elykip@gmail.com")
        self.assertEqual(self.new_.password,"20088")


def test_save_user(self):
        '''
        test_save_user test case to test if the User object is saved into`
        the user list

        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)


def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Test","user","0706274770","test@user@user.com") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2) 

def test_display_user(self):
        '''
        Method that returns a list of all saved users
        ''' 
        self.assertEqual(User.display_users(),User.user_list)





def test_delete_user(self):
        '''

        test_delete_user to test if we can remove a user from our user info

        '''
        self.new_user.save_user()
        test_user = User("Test","user ","0706274770","test@user@user.com") # new 
        test_user.save_user()

        self.new_user.delete_user()# Deleting a user object
        self.assertEqual(len(User.user_list),1)




def test_find_by_number(self):
        '''
        test to check if we can find an user using the number
        '''
        self.new_user.save_user()
        test_user = User("Test","user","0700007800","test@user.com")
        test_user.save_user()
        
        found_user = User.find_by_number("0700007800")
        self.assertEqual(found_user.test_user,test_user.email)


def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("Test","user","0700007800","test@user.com") # new user
        test_user.save_user()
        user_exists = User.user_exist("0700007800")

        self.assertTrue(user_exists)




if __name__ == '__main__':
unittest.main()