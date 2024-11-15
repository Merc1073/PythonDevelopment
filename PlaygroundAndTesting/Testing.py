from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    price: float = 0.0
    in_stock: bool = True

book1 = Book("Title1", "Author1", 59.99, True)
book2 = Book("Title2", "Author2", 45.99, False)

print(book1 == book2)