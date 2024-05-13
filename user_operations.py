class UserManagementSystem:
    def __init__(self):
        self.users = []

    def user_operations(self):
        print('User Operations')
        print('''
        1. Add a new user
        2. View user details
        3. Display all users
        ''')

    def new_user(self):
        name = input('Name: ')
        phone = input('Phone: ')
        password = input('Password: ')
        a_user = UserManagementSystem(name, phone, password)
        self.users.append(a_user)
        print(f'Welcome {name}')

    def user_details(self):
        name = input('Enter user name: ')
        for user in self.users:
            if user.name == name:
                print(f'Name: {user.name}')
                print(f'Phone: {user.phone}')
                return
        print('User not found.')

    def all_users(self):
        if self.users: 
            print("All users:")
            for user in self.users:
                print(f'Name: {user.name}, Phone: {user.phone}')
        else:
            print('No users found.')

    def main(self):
        while True:
            self.user_operations()
            choice = input('Enter your choice: ')
            if choice == '1':
                self.new_user()
            elif choice == '2':
                self.user_details()
            elif choice == '3':
                self.all_users()
            else:
                print('Invalid choice')

if __name__ == "__main__":
    user_menu = UserManagementSystem()
    user_menu.main()