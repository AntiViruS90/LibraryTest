import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))


class TestLibrary:
    def __init__(self, library):
        self.library = library
        self.test_file = "test_library.json"
        self.library.filename = self.test_file  # Для тестов используем отдельный файл

    def clear(self):
        """Удаляет файл с данными после тестов, чтобы не оставить мусор."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_book(self):
        """Тестируем добавление книги."""

        self.library.add_book("Тестовая книга", "Тестовый автор", 2024)
        self.library.load_books()

        assert len(self.library.books) == 1, "Книга не была добавлена!"
        assert self.library.books[0].title == "Тестовая книга", "Название книги не соответствует!"
        assert self.library.books[0].author == "Тестовый автор", "Автор книги не соответствует!"
        assert self.library.books[0].year == 2024, "Год издания книги не соответствует!"
        assert self.library.books[0].status == "в наличии", "Статус книги неверный!"

    def test_delete_book(self):
        """Тестируем удаление книги."""
        book_id_to_delete = self.library.books[0].id
        self.library.add_book("Удаленная книга", "Автор удаления", 2024)
        self.library.load_books()
        self.library.delete_book(book_id_to_delete)

        self.library.load_books()

        assert len(self.library.books) == 1, "Неудаленная книга осталась в списке!"
        assert self.library.books[0].id == 2, f"Осталась неправильная книга с ID={self.library.books[0].id}!"
        assert self.library.books[0].title == "Удаленная книга", "Не та книга осталась после удаления!"

        try:
            self.library.delete_book(999)
        except ValueError as e:
            assert str(
                e) == "Книга с id 999 не найдена.", f"Ожидалась ошибка с сообщением 'Книга с id 999 не найдена.', " \
                                                    f"но ошибка: {e}"

    def test_search_books(self):
        """Тестируем поиск книг."""
        self.library.add_book("Поиск по названию", "Автор поиска", 2023)
        self.library.add_book("Поиск по автору", "Автор поиска", 2022)

        results = self.library.search_books("Поиск")
        assert len(results) == 2, "Поиск по названию не дал нужных результатов!"

        results = self.library.search_books("Автор поиска")
        assert len(results) == 2, "Поиск по автору не дал нужных результатов!"

        results = self.library.search_books("2023")
        assert len(results) == 1, "Поиск по году не дал нужных результатов!"

        results = self.library.search_books("Не существует")
        assert len(results) == 0, "Поиск по несуществующему запросу должен вернуть пустой список!"

    def test_change_book_status(self):
        """Тестируем изменение статуса книги."""
        self.library.add_book("Книга со статусом", "Автор статуса", 2024)
        book_id = self.library.books[0].id

        self.library.change_book_status(book_id, "выдана")
        assert self.library.books[0].status == "выдана", "Статус книги не изменился на 'выдана'!"

        try:
            self.library.change_book_status(book_id, "неверный статус")
        except ValueError as e:
            assert str(
                e) == "Неверный статус. Доступные статусы: 'в наличии', 'выдана'.", f"Ожидалась ошибка с сообщением 'Неверный статус...', но ошибка: {e}"

        self.library.change_book_status(book_id, "в наличии")
        assert self.library.books[0].status == "в наличии", "Статус книги не изменился на 'в наличии'!"

    def test_display_books(self):
        """Тестируем отображение книг."""
        self.library.add_book("Книга для отображения", "Автор отображения", 2024)
        book_id = self.library.books[0].id
        # Проверяем, что метод display_books выводит данные на экран
        # Здесь мы не можем проверить вывод на экран напрямую без перенаправления вывода,
        # но можно проверить, что метод отработал без ошибок
        try:
            self.library.display_books()
        except Exception as e:
            assert False, f"Метод display_books выбросил ошибку: {e}"

    def run_tests(self):
        """Запуск всех тестов."""
        self.test_add_book()
        self.test_delete_book()
        self.test_search_books()
        self.test_change_book_status()
        self.test_display_books()
        print("Все тесты пройдены успешно!")


if __name__ == "__main__":
    from main import Library

    library = Library()
    test_library = TestLibrary(library)
    test_library.run_tests()
    test_library.clear()
