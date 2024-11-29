from typing import List, Optional
from library.models import Book
from library.storage import load_books, save_books


def add_book(title: str, author: str, year: int) -> Book:
    books = load_books()
    new_id = max([book.book_id for book in books], default=0) + 1
    new_book = Book(new_id, title, author, year)
    books.append(new_book)
    save_books(books)
    return new_book


def delete_book(book_id: int) -> bool:
    books = load_books()
    updated_books = [book for book in books if book.book_id != book_id]
    if len(books) == len(updated_books):
        return False  # Книга не найдена
    save_books(updated_books)
    return True


def find_books(query: str) -> List[Book]:
    books = load_books()
    return [
        book
        for book in books
        if query.lower() in book.title.lower()
        or query.lower() in book.author.lower()
        or query == str(book.year)
    ]


def update_status(book_id: int, status: str) -> Optional[Book]:
    books = load_books()
    for book in books:
        if book.book_id == book_id:
            book.status = status
            save_books(books)
            return book
    return None
