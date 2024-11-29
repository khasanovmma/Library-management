import unittest
from library.models import Book
from library.services import add_book, delete_book, find_books, update_status
from library.storage import load_books, save_books


class TestLibraryManagement(unittest.TestCase):

    def setUp(self):
        """
        Создаем тестовые данные перед каждым тестом.
        """
        self.test_books = [
            Book(book_id=1, title="Book One", author="Author A", year=2001),
            Book(
                book_id=2,
                title="Book Two",
                author="Author B",
                year=2002,
                status="выдана",
            ),
        ]
        save_books(self.test_books)  # Сохраняем тестовые данные в файл

    def tearDown(self):
        """
        Удаляем тестовые данные после каждого теста.
        """
        save_books([])  # Очищаем файл данных

    def test_add_book(self):
        """
        Тест добавления новой книги.
        """
        new_book = add_book(title="Book Three", author="Author C", year=2003)
        books = load_books()
        self.assertEqual(len(books), 3)
        self.assertEqual(new_book.title, "Book Three")
        self.assertEqual(new_book.author, "Author C")
        self.assertEqual(new_book.year, 2003)
        self.assertEqual(new_book.status, "в наличии")

    def test_delete_book(self):
        """
        Тест удаления книги по ID.
        """
        result = delete_book(book_id=1)
        books = load_books()
        self.assertTrue(result)
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].book_id, 2)

        # Удаление несуществующей книги
        result = delete_book(book_id=99)
        self.assertFalse(result)

    def test_find_books(self):
        """
        Тест поиска книг по названию, автору или году.
        """
        books_by_title = find_books(query="Book One")
        self.assertEqual(len(books_by_title), 1)
        self.assertEqual(books_by_title[0].title, "Book One")

        books_by_author = find_books(query="Author B")
        self.assertEqual(len(books_by_author), 1)
        self.assertEqual(books_by_author[0].author, "Author B")

        books_by_year = find_books(query="2002")
        self.assertEqual(len(books_by_year), 1)
        self.assertEqual(books_by_year[0].year, 2002)

        books_not_found = find_books(query="Nonexistent")
        self.assertEqual(len(books_not_found), 0)

    def test_update_status(self):
        """
        Тест обновления статуса книги.
        """
        updated_book = update_status(book_id=1, status="выдана")
        self.assertIsNotNone(updated_book)
        self.assertEqual(updated_book.status, "выдана")

        # Проверяем, что обновленный статус сохраняется
        books = load_books()
        self.assertEqual(books[0].status, "выдана")

        # Обновление статуса несуществующей книги
        updated_book = update_status(book_id=99, status="в наличии")
        self.assertIsNone(updated_book)

    def test_load_books(self):
        """
        Тест загрузки всех книг.
        """
        books = load_books()
        self.assertEqual(len(books), 2)
        self.assertEqual(books[0].title, "Book One")
        self.assertEqual(books[1].status, "выдана")


if __name__ == "__main__":
    unittest.main()
