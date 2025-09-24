
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False



class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []



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
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"[{book.book_id}] {book.title} by {book.author} - {status}")

    def display_patrons(self):
        print("\nRegistered Patrons:")
        for patron in self.patrons.values():
            print(f"Patron ID: {patron.patron_id}, Name: {patron.name}")



if __name__ == "__main__":
    library = Library()


    library.add_book(1, "1984", "George Orwell")
    library.add_book(2, "To Kill a Mockingbird", "Harper Lee")


    library.register_patron(101, "Alice")
    library.register_patron(102, "Bob")


    library.borrow_book(101, 1)
    library.borrow_book(102, 2)
    library.return_book(101, 1)


    library.display_books()
    library.display_patrons()
