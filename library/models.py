from dataclasses import dataclass, asdict
from typing import Literal


@dataclass
class Book:
    book_id: int
    title: str
    author: str
    year: int
    status: Literal["в наличии", "выдана"] = "в наличии"

    def to_dict(self) -> dict:
        """
        Converts the Book instance to a dictionary.
        """
        return asdict(self)

    @staticmethod
    def from_dict(data: dict) -> "Book":
        """
        Creates a Book instance from a dictionary.
        """
        return Book(**data)
