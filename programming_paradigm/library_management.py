class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    def check_out(self):
        self._is_checked_out = True

class Library:
    def __init__(self):
        self._books = []

    def add_book(self,book):
        self._books.append(book)

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book._is_checked_out = False
                print(f"You have returned '{title}'")
            return
    print(f"'{title}' was not checked out or does not exist in the library.")

    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
            print(f"You have checked out'{title}'")
        return