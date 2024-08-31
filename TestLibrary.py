import unittest
from LibraryManagement import Book,Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
            self.library = Library()
            
    def test_add_book_success(self):
        
        self.assertIn("1234567890", self.library.books)

if __name__ == "__main__":
    unittest.main()




