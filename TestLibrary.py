import unittest
from LibraryManagement import Book,Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
            self.library = Library()
            self.library.add_book("1234567890", "Rich Dad Poor Dad", "Robert Kiyosaki", 2000)
            self.library.add_book("2345678901", "The Psychology of Money", "Morgan Housel", 20001)

            
    def test_add_book_success(self):
        
        self.assertIn("1234567890", self.library.books)

if __name__ == "__main__":
    unittest.main()




