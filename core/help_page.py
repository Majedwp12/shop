from shop.function import *
from conf import *
def help(edeite):
    if edeite == 'Add product' or edeite == '1':
        enter_user = input('enter name product? ').lower()
        addـproduct(enter_user, bye_list)
        print('Product added successfully')
    elif edeite == 'Remove the product' or edeite == '2':
        remover_product = input('What product do you want to delete?')
        remove_product(remover_product, bye_list)
        pass
    elif edeite == 'View shopping list' or edeite == '3':
        view_shopping(bye_list)

    elif edeite == 'Final registration' or edeite == '4':
        print('The product basket has been registered')
    else:
        print('somthing is worng')


# def go_help():
#     help_method = ('''What do you want?
#         1.Add product
#         2.Remove the product
#         3.View shopping list
#         4.Final registration ''')
#     return help_method


def help_app():
    while True:
        pass