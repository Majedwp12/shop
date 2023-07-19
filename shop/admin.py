import logging
import csv
from conf.log import *


class Product:
    logger = logging.getLogger(__name__)
    def __init__(self, group: str, name: str, price: int, stock: bool) -> None:
        self.group = group
        self.name = name
        self.price = price
        self.stock = stock

    def productـregistration(self, namefile='Warehouse.csv'):
        Product_Information = [self.group, self.name, self.price, self.stock]
        with open(namefile, 'a', newline='') as out:
            writer = csv.writer(out)
            writer.writerow(Product_Information)


def View_warehouse():
    with open(namefile='Warehouse.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            group, name, price, stock = row[0], row[1], row[2], row[3]
            print(
                f'Group : `{group}` , Name : `{name}` , Price : `{price}`, Stock : `{stock}`')
