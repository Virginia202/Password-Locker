from user import User
import random

def create_user(username,number,email,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,number,email,password)
    return new_user

def save_new_user(user):
    '''
    Function to save user
    '''
    user.save_user()


def del_user (user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(number):
    '''
    Function that finds a user by number and returns the user
    '''
    return User.find_by_number(number)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def check_existing_users(number):
    '''
    Function that check if a users exists with that number and return a Boolean
    '''
    return User.user_exist(number)    


def main():
    print("Hello Welcome to the Password locker.Write your name then press enter")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("ca - create user account,  da - Display users, fa -find a user account, ex -exit from the password locker  ")
        short_code = input(">>>").lower()
        print('\n')
        if short_code == "ca":
            print ("New User")
            print("-"* 100)

            print ("Enter first name....")
            f_name = input(">>>")

            print ("Enter last name...")
            l_name = input(">>>")
            

            print ("Enter user email address...")
            acc_address = input (">>>")

            print ("Enter the account password...")
            acc_password = input (">>>")
            print('\n')

            save_new_user(create_user(f_name, l_name, acc_address,acc_password)) # create and save new user.
            print('\n')
            print (f"New user account {f_name} {f_name} created")
            print('\n')


        elif short_code == 'da':  
            if display_users():
                print("Here is the list of users..")
                print('\n')

                for user in display_users():
                    print(f"{user.username} {user.number} {user.email}.....{user.password}")
                    
                    print('\n')
            else:
                print('\n')
                print("You don't have an account")
                print('\n')


        elif short_code == 'fa':

            print("Enter the number you want to search for")


            search_number = input()
            if check_existing_users(search_number):
                search_user = find_user(search_number)
                print(f"{search_user.first_name} {search_user.last_name}")
                print('-' * 10)

                print(f"Phone number.......{search_user.number}")
                print(f"Email address.......{search_user.email}")
            else:
                                    print("User does not exist")

        elif short_code == "ex":
                            print("Bye .......")
                            break
        else:
                            print("use the short code")


if __name__ == '__main__':

    main()
                     