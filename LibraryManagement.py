class Book:
    def __init__(self, isbn, title, author, publication_year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True

class Library:
    def __init__(self):
        self.books = {}
        
    def add_book(self, isbn, title, author, publication_year):
        """Add a new book to the library."""
        if isbn in self.books:
            raise ValueError("Book with ISBN {} already exists.".format(isbn))
        book = Book(isbn, title, author, publication_year)
        self.books[isbn] = book

