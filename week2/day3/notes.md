# SQLAlchemy
- SQLAlchemy is the premier ORM (object-relaitonal mapper) in the python ecosystem
- been in active development for over a decade w/ millions of users
---

# Class and Instance Variables 
Example:  
```python
class Book:
    def __init__(self, title, series, author):
        self._title = title
        self._series = series
        self._author = author

    def __repr__(self):
        return f"{self._title} by {self._author}"

fellowship_of_the_ring = Book(
    "The Fellowship of the Ring",
    "The Lord of the Rings",
    "J.R.R. Tolkien")
grapes_of_wrath = Book(
    "The Grapes of Wrath",
    None,
    "John Steinbeck")

print(fellowship_of_the_ring)  # The Fellowship of the Ring by J.R.R. Tolkien
print(grapes_of_wrath)  # The Grapes of Wrath by John Steinbeck
```  

## Class Variables
- `_title`, `_series`, `_author` are instance variables that are specific to each instane of the `Book` class
  - but what about attrs that need to be shared across instances?

```python
from datetime import date

class Book:
    loan_duration = 14  # days

    def __init__(self, title, series, author):
        self._title = title
        self._series = series
        self._author = author
        self._checked_out_on = None
```  
- while ivars are defined withint the `__init__` method, class vars are defined directly wthin a class
  - `Book.loan_duration` works, but you're more likely to access class vars through the instance `self` 
    - `self.loan_duration`

Recap: 
```python
from datetime import date


class Book:
    loan_duration = 14  # days

    def __init__(self, title, series, author):
        self._title = title
        self._series = series
        self._author = author
        self._checked_out_on = None

    def checkout(self, checked_out_on=date.today()):
        """
        Method to checkout a book.
        """
        self._checked_out_on = checked_out_on

    def is_overdue(self):
        """
        Method to check if a book is overdue.
        """
        overdue = False

        if self._checked_out_on is not None:
            elapsed_days = (date.today() - self._checked_out_on).days
            overdue = elapsed_days > self.loan_duration

        return overdue

    def __repr__(self):
        return f"{self._title} by {self._author}"

fellowship_of_the_ring = Book(
    "The Fellowship of the Ring",
    "The Lord of the Rings",
    "J.R.R. Tolkien")
grapes_of_wrath = Book(
    "The Grapes of Wrath",
    None,
    "John Steinbeck")

print(fellowship_of_the_ring)  # The Fellowship of the Ring by J.R.R. Tolkien
print(grapes_of_wrath)  # The Grapes of Wrath by John Steinbeck

# Check to see if any of the books are overdue.
print(fellowship_of_the_ring.is_overdue())  # False
print(grapes_of_wrath.is_overdue())  # False

# Checkout "The Fellowship of the Ring".
fellowship_of_the_ring.checkout(
    checked_out_on=date.fromisoformat("2020-04-01"))

# Check to see if any of the books are overdue.
print(fellowship_of_the_ring.is_overdue())  # True <-- today's date is at least 14 days past 2020-04-01
print(grapes_of_wrath.is_overdue())  # False

```
## Exploring Attribute Name Lookups within Classes

```python
fellowship_of_the_ring = Book(
    "The Fellowship of the Ring",
    "The Lord of the Rings",
    "J.R.R. Tolkien")
grapes_of_wrath = Book(
    "The Grapes of Wrath",
    None,
    "John Steinbeck")

# Access the `loan_duration` class variable
# from the class instances.
print(fellowship_of_the_ring.loan_duration)  # 14
print(grapes_of_wrath.loan_duration)  # 14
```

Modifying class variable after creating instance updates every existing instance: 
```python
fellowship_of_the_ring = Book(
    "The Fellowship of the Ring",
    "The Lord of the Rings",
    "J.R.R. Tolkien")
grapes_of_wrath = Book(
    "The Grapes of Wrath",
    None,
    "John Steinbeck")

# Access the `loan_duration` class variable
# from the class instances.
print(fellowship_of_the_ring.loan_duration)  # 14
print(grapes_of_wrath.loan_duration)  # 14

# Now change the `loan_duration` class variable value
# through the `Book` class.
Book.loan_duration = 7

# The new `loan_duration` class variable value
# is available on each existing instance.
print(fellowship_of_the_ring.loan_duration)  # 7
print(grapes_of_wrath.loan_duration)  # 7
```

- can only modify class variables on the class itself, NOT through the class variables
  - this would create an INSTANCE VARIABLE, NOT modify the class variable 

```python
# This line of code defines a new instance variable named `loan_duration`.
fellowship_of_the_ring.loan_duration = 3
```

High level overview:
- when accessing a class attr using .notation, Py starts by looking for an ivar w/ that name
  - if an ivar is found, it's returned
  - if not, Py then looks for a class var w/ that name, and returns it
  - if neither, `AttributeError` is thrown 

## Avoiding Attr Name Collisions

- can use `__slots__` class variable to reserve memory for your class' instance variables:

```python
class Book:
    __slots__ = ['_title', '_series', '_author', '_checked_out_on']

    loan_duration = 14  # days

    def __init__(self, title, series, author):
        self._title = title
        self._series = series
        self._author = author
        self._checked_out_on = None
```
- this speeds up Py's ceation of objs 
- defining `__slots__` class var also prevents from dynamically defining attrs

Can't do this:
```python
fellowship_of_the_ring = Book(
    "The Fellowship of the Ring",
    "The Lord of the Rings",
    "J.R.R. Tolkien")

# Attempting to dynamically define an instance variable throws an error:
# AttributeError: 'Book' object has no attribute 'some_variable_name'
fellowship_of_the_ring.some_variable_name = "Oops!"
```

Can't do this either:
```python
class Book:
    # Declaring an instance variable with the name `loan_duration`
    # throws an error:
    # ValueError: 'loan_duration' in __slots__ conflicts with class variable
    __slots__ = ['_title', '_series', '_author', '_checked_out_on',
        'loan_duration']

    loan_duration = 14  # days
```

## Other Ex of Class Vars
- `__module__` is dunder class variable (like `__slots__`) that can be used to get the name of the module that the class is defined w/

```python
print(Book.__module__)  # __main__
```

## Defining/Using a Class Method
- `@classmethod` decorator refs the built-in `classmethod()` fx and is used to define a class method
  - it implicitly takes in an entire class def as its first arm named `cls` 
    - like how instance methods receive an instance of the class thru the implicitly passed `self` arg

```python
@classmethod
def create_series(cls, series, author, *args):
    """
    Factory class method for creating a series of books.
    """
    return [cls(title, series, author) for title in args]

# Call class method to create a series of books.
lord_of_the_rings = Book.create_series(
    "The Lord of the Rings",
    "J.R.R. Tolkien",
    "The Fellowship of the Ring",
    "The Two Towers",
    "The Return of the King")

print(lord_of_the_rings)
# [The Fellowship of the Ring by J.R.R. Tolkien, The Two Towers by J.R.R. Tolkien, The Return of the King by J.R.R. Tolkien]

# Unpack the lord_of_the_rings list into the individual books.
fellowship_of_the_ring, two_towers, return_of_the_king = lord_of_the_rings

print(fellowship_of_the_ring)  # The Fellowship of the Ring by J.R.R. Tolkien
print(two_towers)  # The Two Towers by J.R.R. Tolkien
print(return_of_the_king)  # The Return of the King by J.R.R. Tolkien
```

## Defining/Using a Static Method
- `@staticmethod` decorator refs the built-in `staticmethod()` dx
- similar to a class meth, but doesn't receive a class def thru its first arg

```python
@staticmethod
def get_titles(*args):
    """
    Static method that accepts a variable number
    of Book instances and returns a list of their titles.
    """
    return [book._title for book in args]

# Call the static `Book.getTitles()` method
# to get a list of the book titles.
book_titles = Book.get_titles(
    fellowship_of_the_ring,
    two_towers,
    return_of_the_king)

print(", ".join(book_titles))
# The Fellowship of the Ring, The Two Towers, The Return of the King
```

The entire `Book` class ex:
```python
from datetime import date


class Book:
    loan_duration = 14  # days

    def __init__(self, title, series, author):
        self._title = title
        self._series = series
        self._author = author
        self._checked_out_on = None

    def checkout(self, checked_out_on=date.today()):
        """
        Method to checkout a book.
        """
        self._checked_out_on = checked_out_on

    def is_overdue(self):
        """
        Method to check if a book is overdue.
        """
        overdue = False

        if self._checked_out_on is not None:
            elapsed_days = (date.today() - self._checked_out_on).days
            overdue = elapsed_days > self.loan_duration

        return overdue

    def __repr__(self):
        return f"{self._title} by {self._author}"

    @classmethod
    def create_series(cls, series, author, *args):
        """
        Factory class method for creating a series of books.
        """
        return [cls(title, series, author) for title in args]

    @staticmethod
    def get_titles(*args):
        """
        Static method that accepts a variable number
        of Book instances and returns a list of their titles.
        """
        return [book._title for book in args]


# Call class method to create a series of books.
lord_of_the_rings = Book.create_series(
    "The Lord of the Rings",
    "J.R.R. Tolkien",
    "The Fellowship of the Ring",
    "The Two Towers",
    "The Return of the King")

print(lord_of_the_rings)
# [The Fellowship of the Ring by J.R.R. Tolkien, The Two Towers by J.R.R. Tolkien, The Return of the King by J.R.R. Tolkien]

# Unpack the lord_of_the_rings list into the individual books.
fellowship_of_the_ring, two_towers, return_of_the_king = lord_of_the_rings

print(fellowship_of_the_ring)  # The Fellowship of the Ring by J.R.R. Tolkien
print(two_towers)  # The Two Towers by J.R.R. Tolkien
print(return_of_the_king)  # The Return of the King by J.R.R. Tolkien

# Call the static `Book.getTitles()` method
# to get a list of the book titles.
book_titles = Book.get_titles(
    fellowship_of_the_ring,
    two_towers,
    return_of_the_king)

print(", ".join(book_titles))
# The Fellowship of the Ring, The Two Towers, The Return of the King

# Checkout the first book in the series.
fellowship_of_the_ring.checkout(
    checked_out_on=date.fromisoformat("2020-04-01"))

# Check to see if any of the books are overdue.
print(fellowship_of_the_ring.is_overdue())  # True <-- today's date is at least 14 days past 2020-04-01
print(two_towers.is_overdue())  # False
print(return_of_the_king.is_overdue())  # False
```