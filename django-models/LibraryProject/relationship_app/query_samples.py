from django.db import models
from .models import Author, Book, Library, Librarian

# Has sample data creation and queries for a Django application with models for authors, books, libraries, and librarians.

def create_sample_data():
    # Create authors
    author1 = Author.objects.create(name="George Orwell")
    author2 = Author.objects.create(name="J.K. Rowling")
    
    # Create books
    book1 = Book.objects.create(title="1984", author=author1)
    book2 = Book.objects.create(title="Animal Farm", author=author1)
    book3 = Book.objects.create(title="Harry Potter", author=author2)
    
    # Create libraries
    library1 = Library.objects.create(name="Central Library")
    library1.books.add(book1, book2)
    
    library2 = Library.objects.create(name="City Library")
    library2.books.add(book1, book3)
    
    # Create librarians
    Librarian.objects.create(name="Alice Smith", library=library1)
    Librarian.objects.create(name="Bob Johnson", library=library2)

# 1. Query all books by a specific author
def query_books_by_author(author_name):
    return Book.objects.filter(author__name=author_name)

# 2. List all books in a library
def query_books_in_library(library_name):
    return Library.objects.get(name=library_name).books.all()

# 3. Retrieve the librarian for a library
def query_librarian_for_library(library_name):
    return Librarian.objects.get(library__name=library_name)
