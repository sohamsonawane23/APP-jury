print("soham sonawane")
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return True
        else:
            return False

    def return_book(self):
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"'{self.title}' by {self.author} - {status}"


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"Sorry, {book.title} is currently not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} did not borrow {book.title}")

    def view_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"  - {book.title} by {book.author}")
        else:
            print(f"{self.name} has not borrowed any books.")


# Example usage:
book1 = Book("To Kill a Mockingbird", "Harper Lee")
book2 = Book("1984", "George Orwell")
book3 = Book("Pride and Prejudice", "Jane Austen")

member = Member("Alice")

member.borrow_book(book1)
member.borrow_book(book2)
member.view_borrowed_books()

member.return_book(book1)
member.view_borrowed_books()

member.borrow_book(book3)
member.view_borrowed_books()
