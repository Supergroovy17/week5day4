

class BookManagementSystem:
    def __init__(self):
        self.library = []
        self.borrowed_books = []

    def book_menu(self):
        print('      Book Operations')
        print(''' 
        1. Add a new book
        2. Borrow a book
        3. Return a book
        4. Search for a book
        5. Display all books
        6. Quit
              ''')
#1
    def enter_book(self, collection='collection.txt'):
        try:
            with open(collection, 'a') as file:
                for book in self.library:
                    file.write(f"{book['Book']}|{book['Author']}\n")
        except Exception as e:
            print(f"Error occurred while writing to file: {e}")

    def new_book(self):
        book = input("What book are we adding? ")
        author = input("Who wrote this book? ")
        self.library.append({'Book': book, 'Author': author})
        self.enter_book()
        print(f"Added {book} to your library!")
#borrow book and retun a book still need to print library of what the user hasvs what the library has .
    def borrow_book(self):
        if not self.library:
            print("Library is empty. No books to borrow.")
            return

        book_index = int(input("Enter the index of the book you want to borrow: "))

        if book_index < 0 or book_index >= len(self.library):
            print("Invalid index. Please enter a valid index.")
            return

        borrowed_book = self.library.pop(book_index)
        self.borrowed_books.append(borrowed_book)
        print(f"You have borrowed '{borrowed_book['Book']}' by {borrowed_book['Author']}")

    def return_book(self):
        
        if not self.borrowed_books:
            print("You haven't borrowed any books.")
            return

        book_index = int(input("Enter the index of the book you want to return: "))

        if book_index < 0 or book_index >= len(self.borrowed_books):
            print("Invalid index. Please enter a valid index.")
            return

        returned_book = self.borrowed_books.pop(book_index)
        self.library.append(returned_book)
        print(f"You have returned '{returned_book['Book']}' by {returned_book['Author']}")

    def search_book(self):
        if not self.library:
            print("Library is empty.")
            return

        search_query = input("Enter the book title or author to search: ").lower()
        found_books = []

        for book in self.library:
            if search_query in book['Book'].lower() or search_query in book['Author'].lower():
                found_books.append(book)

        if not found_books:
            print("No matching books found.")
        else:
            print("Matching books found:")
            for i, found_book in enumerate(found_books):
                print(f"{i + 1}. {found_book['Book']} by {found_book['Author']}")

    def display_library(self):
        if not self.library:
            print("Library is empty.")
            return

        print("Library contents:")
        for i, book in enumerate(self.library):
            print(f"{i + 1}. {book['Book']} by {book['Author']}")
    
    def main(self):
        while True:
            self.book_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.new_book()
            elif choice == '2':
                self.borrow_book()
            elif choice == '3':
                self.return_book()
            elif choice == '4':
                self.search_book()
            elif choice == '5':
                self.display_library()
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    book_system = BookManagementSystem()
    book_system.main()