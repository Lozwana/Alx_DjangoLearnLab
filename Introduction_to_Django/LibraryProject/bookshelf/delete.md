# Command
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
list(Book.objects.all())  # Retrieve all books to confirm deletion

# Output
[]