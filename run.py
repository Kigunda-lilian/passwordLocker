#!/usr/bin/env python3.9

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