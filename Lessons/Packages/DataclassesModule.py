import dataclasses
from dataclasses import dataclass, FrozenInstanceError


# normal class
@dataclass
class Point:
    x: int
    y: int


point1 = Point(1, 2)
point2 = Point(3, 4)

print(point1)
print(point1 == point2)


# immutable class (frozen=True)
@dataclass(frozen=True)
class Point2:
    x: int
    y: int


point3 = Point2(10, 20)

try:
    point3.x = 30
except FrozenInstanceError:
    print("You cannot assign that value to an immutable class variable (read only)")


@dataclass
class Book:
    title: str
    author: str
    price: float = 0.0
    in_stock: bool = True

book1 = Book("Title1", "Author1", 59.99, True)
book2 = Book("Title2", "Author2", 45.99, False)

print(book1 == book2)