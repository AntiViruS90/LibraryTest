import json
import os


class Book:
    """
    Класс для представления книги в библиотеке.
    """

    def __init__(self, title, author, year):
        self.id = None
        self.title = title
        self.author = author
        self.year = year
        self.status = "в наличии"

    def to_dict(self):
        """Преобразует объект книги в словарь для записи в JSON."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        """Создает объект книги из словаря, считанного из JSON."""
        book = Book(data["title"], data["author"], data["year"])
        book.id = data["id"]
        book.status = data["status"]
        return book


class Library:
    """
    Класс для управления библиотекой книг.
    """

    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        """Загружает книги из файла, если он существует."""
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Book.from_dict(book) for book in data]
        else:
            return []

    def save_books(self):
        """Сохраняет книги в файл."""
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title, author, year):
        """Добавляет книгу в библиотеку."""
        book = Book(title, author, year)
        book.id = self.generate_id()
        self.books.append(book)
        self.save_books()

    def generate_id(self):
        """Генерирует уникальный идентификатор для книги."""
        return max([book.id for book in self.books], default=0) + 1

    def delete_book(self, book_id):
        """Удаляет книгу по id."""
        book_to_delete = self.find_book_by_id(book_id)
        if book_to_delete:
            self.books.remove(book_to_delete)
            self.save_books()
        else:
            raise ValueError(f"Книга с id {book_id} не найдена.")

    def find_book_by_id(self, book_id):
        """Находит книгу по id."""
        return next((book for book in self.books if book.id == book_id), None)

    def search_books(self, search_term):
        """Ищет книги по title, author или year."""
        return [book for book in self.books if search_term.lower() in book.title.lower() or
                search_term.lower() in book.author.lower() or search_term in str(book.year)]

    def change_book_status(self, book_id, new_status):
        """Меняет статус книги на "в наличии" или "выдана"."""
        if new_status not in ["в наличии", "выдана"]:
            raise ValueError("Неверный статус. Доступные статусы: 'в наличии', 'выдана'.")
        book_to_update = self.find_book_by_id(book_id)
        if book_to_update:
            book_to_update.status = new_status
            self.save_books()
        else:
            raise ValueError(f"Книга с id {book_id} не найдена.")

    def display_books(self):
        """Отображает все книги в библиотеке."""
        if not self.books:
            print("Библиотека пуста.")
            return
        for book in self.books:
            print(
                f"ID: {book.id}, \nНазвание: {book.title}, \nАвтор: {book.author}, \nГод издания: {book.year}, "
                f"\nСтатус: {book.status}")
            print("############################")


def main():
    """
        Основная функция приложения для управления библиотекой книг.
        Отображает меню и обрабатывает выбранные пользователем действия.

        Параметры:
        Нет

        Возвращает:
        Нет
    """
    library = Library()

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Выберите действие (1-6): ")

        try:
            if choice == "1":
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                year = input("Введите год издания книги: ")
                library.add_book(title, author, int(year))
                print("Книга добавлена.")

            elif choice == "2":
                book_id = int(input("Введите id книги для удаления: "))
                library.delete_book(book_id)
                print("Книга удалена.")

            elif choice == "3":
                search_term = input("Введите текст для поиска: ")
                results = library.search_books(search_term)
                if results:
                    print("Найденные книги:")
                    for book in results:
                        print(
                            f"ID: {book.id}, \nНазвание: {book.title}, \nАвтор: {book.author}, \nГод издания: {book.year}, \nСтатус: {book.status}")
                else:
                    print("Книги не найдены.")

            elif choice == "4":
                library.display_books()

            elif choice == "5":
                book_id = int(input("Введите id книги для изменения статуса: "))
                new_status = input("Введите новый статус (в наличии/выдана): ")
                library.change_book_status(book_id, new_status)
                print(f"Статус книги изменен на '{new_status}'.")

            elif choice == "6":
                print("Выход из программы.")
                break

            else:
                print("Неверный выбор. Попробуйте снова.")

        except ValueError as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
