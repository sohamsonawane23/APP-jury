# Class for Book
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"[{self.book_id}] {self.title} by {self.author} - {status}"


# Class for Patron
class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"Patron ID: {self.patron_id}, Name: {self.name}"


# Class for Library Management
class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            print("Book ID already exists.")
        else:
            self.books[book_id] = Book(book_id, title, author)
            print(f"Book '{title}' added successfully.")

    def register_patron(self, patron_id, name):
        if patron_id in self.patrons:
            print("Patron ID already exists.")
        else:
            self.patrons[patron_id] = Patron(patron_id, name)
            print(f"Patron '{name}' registered successfully.")

    def borrow_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print("Patron not registered.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        patron = self.patrons[patron_id]
        book = self.books[book_id]

        if book.is_borrowed:
            print("Book is already borrowed.")
        else:
            book.is_borrowed = True
            patron.borrowed_books.append(book)
            print(f"Book '{book.title}' borrowed by {patron.name}.")

    def return_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print("Patron not registered.")
            return
        if book_id not in self.books:
            print("Book not found.")
            return

        patron = self.patrons[patron_id]
        book = self.books[book_id]

        if book in patron.borrowed_books:
            book.is_borrowed = False
            patron.borrowed_books.remove(book)
            print(f"Book '{book.title}' returned by {patron.name}.")
        else:
            print(f"{patron.name} did not borrow the book '{book.title}'.")

    def display_books(self):
        print("\nBooks in Library:")
        for book in self.books.values():
            print(book)

    def display_patrons(self):
        print("\nRegistered Patrons:")
        for patron in self.patrons.values():
            print(patron)


# Sample usage
if __name__ == "__main__":
    library = Library()

    # Adding books
    library.add_book(1, "1984", "George Orwell")
    library.add_book(2, "To Kill a Mockingbird", "Harper Lee")

    # Registering patrons
    library.register_patron(101, "Alice")
    library.register_patron(102, "Bob")

    # Borrowing and returning books
    library.borrow_book(101, 1)
    library.borrow_book(102, 2)
    library.return_book(101, 1)

    # Displaying library state
    library.display_books()
    library.display_patrons()
