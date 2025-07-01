library = []

def _print_book_info(book: dict[str, int | str | bool]):
    availability = "Available" if book['available'] else "Not Available"
    return f"Book \"{book['title']}\" by {book['author']} published in {book['year_of_publication']}, ISBN: {book['isbn']}. ({availability})"

def add_book():
    title = input("Enter the title of the book: ").strip()
    author = input("Enter the name of the author of the book: ").strip()
    year_of_publication = int(input("Enter the year of publication of the book: "))
    isbn = input("Enter the Book ISBN: ").strip()
    book = {"title": title, "author": author, "year_of_publication": year_of_publication, "isbn": isbn, "available": True}
    library.append(book)
    return f"{_print_book_info(book)}"


def view_books():
    for idx, book in enumerate(library, start=1):
        print(f"{idx}. {_print_book_info(book)}")

def update_book(isbn):
    for book in library:
        if book['isbn'] == isbn:
            print("Book found. Details: ")
            print(_print_book_info(book))
            # title = input(f"Enter the title of the book or leave blank to use '{book['title']}': ").strip()
            # author = input(f"Enter the name of the author of the book or leave blank to use '{book['author']}': ").strip()
            # year_of_publication = int(input(f"Enter the year of publication of th or leave blank to use '{book['year_of_publication']}'"))
            # _isbn = input(f"Enter the Book ISBN or leave blank to use '{book['isbn']}': ").strip()

            # if title:
            #     book['title'] = title
            # if author:
            #     book['author'] = author
            # if year_of_publication:
            #     book['year_of_publication'] = year_of_publication
            # if _isbn:
            #     book['isbn'] = _isbn

            title = input(f"Enter the title of the book or leave blank to use '{book['title']}': ").strip() or book['title']
            author = input(f"Enter the name of the author of the book or leave blank to use '{book['author']}': ").strip() or book['author']
            year_of_publication = int(input(f"Enter the year of publication of th or leave blank to use '{book['year_of_publication']}': ")) or book['year_of_publication']
            _isbn = input(f"Enter the Book ISBN or leave blank to use '{book['isbn']}': ").strip() or book['isbn']

            original_book = book.copy()

            book['title'] = title
            book['author'] = author
            book['year_of_publication'] = year_of_publication
            book['isbn'] = _isbn

            return f"{_print_book_info(original_book)} has been updated to {_print_book_info(book)}"
    return f"Book with ISBN {isbn} not found"


def delete_book(isbn):
    # for idx, book in enumerate(library):
    for book in library:
        if book['isbn'] == isbn:
            print("Book found. Details: ")
            print(_print_book_info(book))
            # del library[idx]
            # library.pop(idx)
            library.remove(book)
            return f"{_print_book_info(book)} has been deleted successfully"
    return f"Book with ISBN {isbn} not found"
        
def search_book(title: str):
    for book in library:
        if book['title'].lower() == title.lower():
            print("Book found. Details: ")
            return _print_book_info(book)
            
    return f"Book with title {title} not found"


def borrow_book(isbn):
    for book in library:
        if book['isbn'] == isbn:
            print("Book found. Details: ")
            print(_print_book_info(book))
            if book['available']:
                book['available'] = False
                return f"{_print_book_info(book)} has been borrowed successfully"
            return f"{_print_book_info(book)} is not available"
    return f"Book with ISBN {isbn} not found"


def return_book(isbn):
    for book in library:
        if book['isbn'] == isbn:
            print("Book found. Details: ")
            print(_print_book_info(book))
            if not book['available']:
                book['available'] = True
                return f"{_print_book_info(book)} has been returned successfully"
            return f"{_print_book_info(book)} is already available"
    return f"Book with ISBN {isbn} not found"



menu = """
1. Add Book
2. View Books
3. Update Book
4. Delete Book
5. Search Book
6. Borrow Book
7. Return Book
8. Exit
"""

print("Welcome to our Library")

while True:
    print(menu)
    choice = input("Choose an option from the menu above: ").strip()
    
    if choice == "1":
        print(add_book())
    elif choice == "2":
        view_books()
    elif choice == "3":
        isbn = input("Enter the ISBN of the book you want to update: ").strip()
        print(update_book(isbn))
    elif choice == "4":
        isbn = input("Enter the ISBN of the book you want to delete: ").strip()
        print(delete_book(isbn))
    elif choice == "5":
        title = input("Enter the title of the book you are looking for: ").strip()
        print(search_book(title))
    elif choice == "6":
        isbn = input("Enter the ISBN of the book you want to borrow: ").strip()
        print(borrow_book(isbn))
    elif choice == "7":
        isbn = input("Enter the ISBN of the book you want to return: ").strip()
        print(return_book(isbn))
    elif choice == "8":
        print("Exiting the Library...")
        break
    else:
        print("Invalid choice.")


