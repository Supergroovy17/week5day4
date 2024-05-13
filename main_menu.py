class MainMenu:
    def __init__(self):
        self.current_user = None

    def main_menu(self):
        print('Main Menu')
        print('''
        1. Book Operations 
        2. User Operations
        3. Author Operations
        4. Quit
        ''')

    def user_operations(self):
        from user_operations import UserManagementSystem
        user_system = UserManagementSystem(self.current_user)
        user_system.main()

    def book_operations(self):
        from book_operations import BookManagementSystem
        book_system = BookManagementSystem()
        book_system.main()

    def author_operations(self):
        from author_operations import AuthorManagementSystem
        author_system = AuthorManagementSystem()
        author_system.main()

    def quit_program(self):
        print("Quitting the program. Goodbye!")
        exit()

    def main(self):
        while True:
            self.main_menu()
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.book_operations()
            elif choice == '2':
                self.user_operations()
            elif choice == '3':
                self.author_operations()
            elif choice == '4':
                self.quit_program()
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main_menu = MainMenu()
    main_menu.main()