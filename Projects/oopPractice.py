"""

Objective:

Create a simple Library Management System with the following specifications:

1. Classes:

Book:
Represents a book in the library with attributes for title, author, and availability.

Library:
Manages a collection of books and allows borrowing, returning, and displaying available books.

2. Methods:

Book class:
__init__(self, title, author): Initialize the book with a title, author, and set its availability to True.
__str__(self): Return a string representation of the book's title and author.

Library class:
__init__(self): Initialize an empty collection of books.
add_book(self, book): Adds a book to the library.
display_available_books(self): Displays all books that are currently available in the library.
borrow_book(self, title): Marks a book as borrowed if available. If the book is already borrowed, print a message saying it’s not available.
return_book(self, title): Marks a book as available if it has been borrowed. If it wasn't borrowed, print a message saying it’s already available.

Interactions:

* Add some books to the library.
* Display all available books.
* Borrow and return a book, and verify that the library updates accordingly.

"""

class Book:
    def __init__(self, title, author, availability=True):
        self.title = title
        self.author = author
        self.availability = availability

    def __str__(self):
        return f"{self.title}, written by {self.author}"


class Library:

    available_books = []
    borrowed_books = []

    def __init__(self, name):
        self.name = name

    def add_book(self, new_book):
        self.available_books.append(new_book)
        print(f"Added {new_book} to {self.name}.\n")

    def display_available_books(self):
        for book in self.available_books:
            if book.availability:
                print(f"Available books: {book}.")
        print()

    def borrow_book(self, book_to_borrow):
        if book_to_borrow in self.available_books and book_to_borrow.availability:
            self.borrowed_books.append(book_to_borrow)
            self.available_books.remove(book_to_borrow)
            print(f"Added {book_to_borrow} to borrowed books.\n")
        else:
            print(f"{book_to_borrow.title} is not in available books.\n")

    def return_book(self, book_to_return):
        if book_to_return in self.borrowed_books:
            self.available_books.append(book_to_return)
            self.borrowed_books.remove(book_to_return)
            print(f"Returned {book_to_return.title} to available books.\n")
        else:
            print(f"{book_to_return.title} is not in borrowed books.\n")

library1 = Library("The Epic Library")

book1 = Book("The Midnight Library", "Matt Haig")
book2 = Book("Where the Crawdads Sing", "Delia Owens")
book3 = Book("A Man Called Ove", "Fredrik Backman")

print(book1)

library1.add_book(book1)
library1.add_book(book2)
library1.add_book(book3)

library1.display_available_books()

library1.borrow_book(book1)
library1.display_available_books()

library1.return_book(book1)
library1.display_available_books()





# correct solution
class Book2:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.availability = True  # All books are initially available

    def __str__(self):
        return f"{self.title}, written by {self.author}"


class Library2:
    def __init__(self, name):
        self.name = name
        self.available_books = []  # Instance variable
        self.borrowed_books = []   # Instance variable

    def add_book2(self, new_book):
        self.available_books.append(new_book)
        print(f"Added '{new_book}' to {self.name}.\n")

    def display_available_books2(self):
        print("Available books:")
        for book in self.available_books:
            if book.availability:
                print(f"- {book}")
        print()

    def borrow_book2(self, book_to_borrow):
        if book_to_borrow in self.available_books and book_to_borrow.availability:
            book_to_borrow.availability = False
            print(f"Borrowed '{book_to_borrow}'.\n")
        else:
            print(f"'{book_to_borrow.title}' is not available to borrow.\n")

    def return_book2(self, book_to_return):
        if not book_to_return.availability:
            book_to_return.availability = True
            print(f"Returned '{book_to_return}'.\n")
        else:
            print(f"'{book_to_return.title}' was not borrowed.\n")


# Example usage
library = Library2("City Library")
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

library.add_book2(book1)
library.add_book2(book2)

library.display_available_books2()

library.borrow_book2(book1)
library.display_available_books2()

library.return_book2(book1)
library.display_available_books2()
