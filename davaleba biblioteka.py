class book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year

class library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title == book.title:
                self.books.remove(book)
                break


    def list_books(self):
        for book in self.books:
            print(f"{book.title}, {book.author}, {book.year}")
