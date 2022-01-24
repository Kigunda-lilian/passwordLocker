#!/usr/bin/env python3.9

import email
from User import User
# from credentials import Credential

def create_User(first_name,last_name, password, email):
    '''
    function to create a new user.
    '''
    new_User = User(first_name,last_name, password, email)
    return new_User

def save_User(User):
    '''
    function to save user
    '''
    User.save_User(User)

def delete_User(User):
    '''
    function to delete a user
    '''
    User.delete_User(User)
    
def find_User(first_name):
        '''
    method that takes in the firstname and returns a user that matches that name.
    '''
        return User.find_by_first_name(first_name)
    
def check_existing_User(email):
        '''
    method that checks if a user exists from the  listOfUsers.
    '''
        return User.User_exists(email)   
    
def create_user_details(profile, password):
    
    details = Credential( profile, password)
    return details

def save_user_details(details):
    '''
    function to save user info
    '''
    return Credential.save_profile(details)

def display_all_users():
    '''
    function to display all users
    '''
    return User.display_profile()

def main():
    print("Hey welcome to Password Locker App.What is your name?")
    first_name = input()
    print(f"Hey {first_name}. what would you like to do :)")
    print("\n")
    
    while True:
            print("Use these numbers to choose an option:\n 1. Create an account \n 2. Display available users \n 3. Login to your account \n 5. sign out")
            print("\n")
            
            decision = int(input())
            if decision == 1:
                 print(" Create a new Contact")
                 print("-"*15)

                 print ("First name ....")
                 first_name = input()

                 print("Last name ...")
                 last_name = input()

                 print("Enter password ...")
                 password = input()

                 print("Email address ...")
                 email = input()


                 save_User(create_User(first_name,last_name,password,e_address)) # create and save new contact.
                 print ('\n')
                 print(f"{first_name}, your account has been successfully created.")
                 print ('\n')