import logging
from log_in import main_login
from help_page import help_app
from shop.function import *
from conf import *
from shop.helper.const import (
    EXIT_COMMANDS,
    HELP_COMMANDS,
    ADMIN_COMMANDS
)


logger = logging.getLogger(__name__)


while True:
    enter_user = input('log in or  sing up  or shoping? ').lower()
    logger.info(f'Enter user={enter_user} ')
    if enter_user in ADMIN_COMMANDS:
        main_login()
    elif enter_user in HELP_COMMANDS:
        help_app()
    elif enter_user in EXIT_COMMANDS:
        break
    else:
        addـproduct(enter_user, bye_list)
        print('Product addition was successful')
        print(f'There are *{len(bye_list)}* products in the shopping cart')
