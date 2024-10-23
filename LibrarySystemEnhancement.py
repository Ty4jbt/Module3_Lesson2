# Task 1
# Objective: Update the existing library system by adding new books and insuring no duplicates

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Function to add a new book to the library
def add_book(library, book):

    # Check if the book is not in the library already
    if book not in library:

        # If the book is not in the library, append the book to the library list
        library.append(book)
        print(f'Book {book} has been added to the library.')

    else:

        # If the book is already in the library, print a message
        print(f'Book {book} is already in the library.')

# List of a new book to add to the library and an existing book
new_book = [("The Catcher in the Rye", "J.D. Salinger"), ("1984", "George Orwell")]

# Loop through each book in the new_book list and add it to the library
results = [add_book(library, book) for book in new_book]

# Print the updated library
print(library)