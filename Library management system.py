class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self):
        book_id = input("Enter book ID: ")
        title = input("Enter book title: ")
        author = input("Enter author: ")
        copies = int(input("Enter number of copies: "))
        self.books[book_id] = {'title': title, 'author': author, 'copies': copies}
        print(f"Book '{title}' added to the library.")

    def add_member(self):
        member_id = input("Enter member ID: ")
        name = input("Enter member name: ")
        self.members[member_id] = {'name': name, 'borrowed_books': []}
        print(f"Member '{name}' added.")

    def checkout_book(self):
        member_id = input("Enter member ID: ")
        book_id = input("Enter book ID: ")
        if self.authenticate_member(member_id) and self.book_exists(book_id):
            if self.books[book_id]['copies'] > 0:
                self.members[member_id]['borrowed_books'].append(book_id)
                self.books[book_id]['copies'] -= 1
                print(f"Book '{self.books[book_id]['title']}' checked out by {self.members[member_id]['name']}.")
            else:
                print("No copies available!")
        else:
            print("Invalid member ID or book ID.")

    def return_book(self):
        member_id = input("Enter member ID: ")
        book_id = input("Enter book ID: ")
        if self.authenticate_member(member_id) and book_id in self.members[member_id]['borrowed_books']:
            self.members[member_id]['borrowed_books'].remove(book_id)
            self.books[book_id]['copies'] += 1
            print(f"Book '{self.books[book_id]['title']}' returned by {self.members[member_id]['name']}.")
        else:
            print("Invalid return attempt.")

    def authenticate_member(self, member_id):
        return member_id in self.members

    def book_exists(self, book_id):
        return book_id in self.books

    def display_books(self):
        for book_id, details in self.books.items():
            print(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Copies: {details['copies']}")

def main():
    library = Library()
    while True:
        print("\n1. Add Book")
        print("2. Add Member")
        print("3. Checkout Book")
        print("4. Return Book")
        print("5. Display Books")
        print("0. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            library.add_book()
        elif choice == '2':
            library.add_member()
        elif choice == '3':
            library.checkout_book()
        elif choice == '4':
            library.return_book()
        elif choice == '5':
            library.display_books()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
