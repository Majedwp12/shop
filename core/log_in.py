from account.Create_account import singUp
from account.Log_account import login
from getpass import getpass
from conf import *
from admin_page import main_admin
import logging
logger = logging.getLogger(__name__)


def main_login():
    name_fuc = __name__
    logger.info(f'star use {name_fuc}')
    while True:
        user = input('singUp/Login').lower()
        logger.info(f'Enter user={user} ')
        if user == 'singUp':
            user_name = input('Enter your USER NAME : ')
            user_passworld = input('Enter your PASSWROD :')
            singUp(user_name, user_passworld)
            logger.info(f'The user created an account')
            print('Account creation was successful')
            input('Please enter to go to the next page . . . ')
        elif user == 'Login':
            user_name = input('Enter your USER NAME : ')
            user_passworld = getpass.getpass('Enter your PASSWROD :')
            if login(user_name, user_passworld):
                input('Login in successful ,Please enter to go to the next page . . . ')
                logger.info(f'User requested login')
                main_admin()  # go admin page
