import json
from typing import List
from library.models import Book

FILE_PATH = "data/books.json"


def load_books() -> List[Book]:
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
            return [Book.from_dict(book) for book in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_books(books: List[Book]):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(
            [book.to_dict() for book in books],
            file,
            ensure_ascii=False,
            indent=4,
        )
