import csv
import sys

list_of_users = []


class User:
    name = ""
    address = ""
    phone_number = ""

    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number


def add_user():
    name = input("ENTER NAME:")
    address = input("ENTER ADDRESS:")
    phone_number = input("ENTER PHONE NUMBER:")
    user = User(name, address, phone_number)
    list_of_users.append(user)


def remove_user():
    name = input("ENTER NAME:")
    found = False
    for user in list_of_users:
        if user.name == name:
            found = True
            list_of_users.remove(user)
            print("The user you inputted has been deleted from the phonebook.")

    if not found:
        print("You inputted an non-existent user, which was not deleted from the phonebook. ")


def search_by_name_and_address():
    name = input("ENTER NAME:")
    address = input("ENTER ADDRESS:")
    found = False

    for user in list_of_users:
        if user.name == name and user.address == address:
            # found = True
            return user.phone_number


            # print("The user you are looking for has been found and"
            #       " their phone number is the following:" + user.phone_number)

    if found == False:
        print("The user you are looking for has not been found in this phonebook.")


def main():

    # Read a given csv file.
    with open('docs/users.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            user = User(row[0], row[1], row[2])
            list_of_users.append(user)

    print("Your phonebook now has been updated." + "\n" +
          "Follow the given instructions for what you would like to do next." + "\n" +
          "ENTER 1 if you would like to add a new user." + "\n" +
          "ENTER 2 if you would like to delete an existing user." + "\n" +
          "ENTER 3 if you would like to search a user by their name and address." + "\n" +
          "To exit this, please enter EXIT."
          )
    choice = input("ENTER CHOICE:")
    if choice == "1":
        add_user()
    elif choice == "2":
        remove_user()
    elif choice == "3":
        search_by_name_and_address()
    elif choice == "EXIT":
        sys.exit()
    else:
        print("Your input is not a valid choice.")


if __name__ == "__main__":
    main()
