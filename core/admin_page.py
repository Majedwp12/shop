from shop.admin import *
import logging
logger = logging.getLogger(__name__)

def main_admin():
    name_fuc=__name__
    logger.info(f'star use {name_fuc}')
    admin_order = input('''
                    1.Add 
                    2.View 
                    3.Edit ''').capitalize()
    logger.info(f'admin want `{admin_order}`')
    if admin_order == '1' or admin_order == 'Add':
        group = input('What is the group of the new product?')
        name = input('What is the name of the new product?')
        price = input('What is the price of the new product?')
        stock = input('What is the stock of the new product?')
        Product(group, name, price, stock).productـregistration()
        logger.info(f'admin add product')
    elif admin_order == '2' or admin_order == 'View ':
        logger.info(f'admin View warehouse')
        View_warehouse()
    elif admin_order == '3' or admin_order == 'Edit':
        logger.info(f'admin edit warehouse')
        pass
    else:
        pass
