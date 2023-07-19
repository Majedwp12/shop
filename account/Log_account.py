import csv


def login(username: str, password: str, namefile='user.csv') -> bool:
    flag = False
    with open(namefile, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            username_1 = row[0]
            passworld_1 = row[1]
            if username == username_1 and password == passworld_1:
                flag = True
    return flag