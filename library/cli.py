from library.services import add_book, delete_book, find_books, update_status
from library.storage import load_books


def menu():
    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книги")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("0. Выйти")

        choice = input("Выберите действие: ")
        if choice == "1":
            title = input("Введите название: ")
            author = input("Введите автора: ")
            year = int(input("Введите год издания: "))
            book = add_book(title, author, year)
            print(f"Добавлена книга: {book.to_dict()}")
        elif choice == "2":
            book_id = int(input("Введите ID книги для удаления: "))
            if delete_book(book_id):
                print("Книга успешно удалена.")
            else:
                print("Книга не найдена.")
        elif choice == "3":
            query = input("Введите запрос (название, автор или год): ")
            books = find_books(query)
            for book in books:
                print(book.to_dict())
        elif choice == "4":
            print("Список книг:")
            books = load_books()
            for book in books:
                print(book.to_dict())
        elif choice == "5":
            book_id = int(input("Введите ID книги: "))
            status = input("Введите новый статус ('в наличии' или 'выдана'): ")
            book = update_status(book_id, status)
            if book:
                print(f"Статус обновлен: {book.to_dict()}")
            else:
                print("Книга не найдена.")
        elif choice == "0":
            break
        else:
            print("Неверный выбор, попробуйте снова.")
