class PhoneBook:

    def __init__(self, list_of_users):
        self.list_of_users = list_of_users

    def add_user(self, user_id):
        self.list_of_users.append(user_id)

    def remove_user(self, user_id):
        self.list_of_users.remove(user_id)

    def search_by_name_and_address(self, name, address):
        found = False
        for user in self.list_of_users:
            if user.name == name and user.address == address and found:
                found = True
                print(user.phone_number)

