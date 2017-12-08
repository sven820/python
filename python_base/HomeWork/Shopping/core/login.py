__author__ = "JJ.sven"

import json


'''
users = {
    user_account: {
        pwd: pwd
        name: name
    }
}
'''
users_file_name = 'users.txt'
name_key = 'user'
pwd_key = 'pwd'
users = {}

user_file = open(users_file_name, 'r')
users = json.load(user_file)
user_file.close()

def checkAccount(account, pwd):
    user_info = dict(users.get(account))
    if user_info:
        u_pwd = str(user_info.get(pwd_key))

    else:
        print('无此用户， 请注册')
        return False
    pass

def login(account, pwd):

    pass

def register(account, pwd, name):
    pass

def freeze(account, pwd):
    pass

