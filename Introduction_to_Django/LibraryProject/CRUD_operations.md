# Command
from bookshelf.models import Book
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Output
<Book: 1984>

# Command
book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")

# Output
Title: 1984, Author: George Orwell, Year: 1949

# Command
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
updated_book = Book.objects.get(id=book.id)
print(updated_book.title)

# Output
Nineteen Eighty-Four

# Command
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
list(Book.objects.all())  # Retrieve all books to confirm deletion

# Output
[]