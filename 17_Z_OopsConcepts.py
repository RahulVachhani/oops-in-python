# Oops, desgin patterns in Python
# Write a code which demonstrates the workflow of oops in code.

# Base class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f"'{self.title}' by {self.author}"


# Derived class for Fiction books
class Fiction(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

    def get_info(self):
        return f"Fiction Book: {super().get_info()}, Genre: {self.genre}"


# Derived class for Non-Fiction books
class NonFiction(Book):
    def __init__(self, title, author, subject):
        super().__init__(title, author)
        self.subject = subject

    def get_info(self):
        return f"Non-Fiction Book: {super().get_info()}, Subject: {self.subject}"


# Class to manage the library
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book.get_info())


# Demonstration of OOP workflow
if __name__ == "__main__":
    # Create a library instance
    my_library = Library()

    # Create book instances
    book1 = Fiction("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
    book2 = NonFiction("Sapiens", "Yuval Noah Harari", "History")

    # Add books to the library
    my_library.add_book(book1)
    my_library.add_book(book2)

    # List all books in the library
    print("Books in the library:")
    my_library.list_books()
