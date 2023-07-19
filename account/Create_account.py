import csv


def singUp(input_username: str, input_password: str, namefile='user.csv'):
    out_list = [input_username, input_password]
    with open(namefile, 'a', newline='') as out:
        writer = csv.writer(out)
        writer.writerow(out_list)
