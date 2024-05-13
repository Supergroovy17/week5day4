
class AuthorManagementSystem:
    def __init__(self):
        self.authors = []

    def author_operations(self):
        print('Author Operations')
        print('''    
        1. Add a new author
        2. View author details
        3. Display all authors
        ''')

    def new_author(self):
        author = input("Enter the name of the new author: ")
        self.authors.append(author)
        print(f"Added {author} to the list of authors.")

    def author_details(self):
        author = input("Enter the name of the author you want to view details for: ")
        if author in self.authors:
            print(f"Details for {author}:")

        else:
            print("Author not found.")

    def all_authors(self):
        if self.authors:
            print("all authors:")
            for author in self.authors:
                print(author)
        else:
            print("No authors found.")

    def main(self):
        while True:
            self.author_operations()
            choice = input("Enter your choice (1-3): ")

            if choice == '1':
                self.new_author()
            elif choice == '2':
                self.author_details()
            elif choice == '3':
                self.all_authors()
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")


if __name__ == "__main__":
    author_system = AuthorManagementSystem()
    author_system.main()