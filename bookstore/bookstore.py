class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        
    def get_books(self):
        return self.books
    
    def search_books(self, title=None, author=None):
        results = []
        if title==None:
            for book in self.books:
                if book.author == author:
                    results.append(book)
            return results
        else:
            for book in self.books:
                if title.lower() in book.title.lower():
                    results.append(book)
            return results
        
class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = []
        
    def get_books(self):
        return self.books

class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        author.books.append(self)