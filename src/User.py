import csv

list_of_users = []


class User:
    name = ""
    address = ""
    phone_number = ""

    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number


with open('users.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        pi = User(row[0], row[1], row[2:])
        list_of_users.append(pi)

print(list_of_users)