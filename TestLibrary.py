import unittest
from LibraryManagement import Book,Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
            self.library = Library()
            self.library.add_book("1234567890", "Rich Dad Poor Dad", "Robert Kiyosaki", 2000)
            self.library.add_book("2345678901", "The Psychology of Money", "Morgan Housel", 20001)

            
    def test_add_book_success(self):
        
        self.assertIn("1234567890", self.library.books)
        
    def test_add_book_duplicate_isbn(self):
        
        with self.assertRaises(ValueError):
            self.library.add_book("1234567890", "Book 2", "Author 2", 2021)
            
    def test_borrow_book_success(self):
          
        self.library.borrow_book("1234567890")
        book = self.library.books["1234567890"]
        self.assertFalse(book.is_available)
        
    def test_borrow_book_not_found(self):
        with self.assertRaises(ValueError):
            self.library.borrow_book("invalid isbn")




if __name__ == "__main__":
    unittest.main()




