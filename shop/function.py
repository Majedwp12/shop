import os

bye_list = []
def addـproduct(name: str, namelist: list) -> list:
    '''get name product
    and append product in bye list'''
    namelist.append(name)
    for i in namelist:
        if i == name:
            print('This is a duplicate item')
    namelist = list(dict.fromkeys(namelist))


def remove_product(name: str, namelist: list) -> list:
    if name in namelist:
        namelist.remove(name)
    else:
        print(f'{name} is not a product in the shopping list')


def search_item(name: str, namelist: list):
    if name in namelist:
        print('The product is in the shopping list')
    else:
        print('The product is not in the shopping list')





def view_shopping(bye_list: list) -> str:
    print('This is your shopping list : ')
    for product in bye_list:
        print(f'>{product}')


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


def go_help():
    help_method = ('''What do you want?
        1.Add product
        2.Remove the product
        3.View shopping list
        4.Final registration ''')
    return help_method




def cler_ter():
    os.system('cls' if os.name=='nt' else 'clear')