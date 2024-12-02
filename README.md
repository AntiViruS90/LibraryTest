[![Maintainability](https://api.codeclimate.com/v1/badges/7bc2d4ab6b37e28ecbf6/maintainability)](https://codeclimate.com/github/AntiViruS90/LibraryTest/maintainability)

# Описание классов и методов
## Класс _Book_
### Представляет книгу в библиотеке.

### Методы:

```__init__(self, title, author, year)```: Конструктор. Инициализирует объект книги с заданными названием, автором и годом издания.

```to_dict(self)```: Преобразует объект книги в словарь для записи в JSON.

```from_dict(data)```: Создает объект книги из словаря, считанного из JSON.

## Класс _Library_
### Представляет библиотеку, в которой хранятся книги.

### Методы:

```__init__(self, filename="library.json")```: Конструктор. Инициализирует библиотеку, загружая книги из файла.

```load_books(self)```: Загружает книги из файла, если он существует.

```save_books(self)```: Сохраняет книги в файл.

```add_book(self, title, author, year)```: Добавляет книгу в библиотеку.

```generate_id(self)```: Генерирует уникальный идентификатор для книги.

```delete_book(self, book_id)```: Удаляет книгу по ID.

```find_book_by_id(self, book_id)```: Ищет книгу по ID.

```search_books(self, search_term)```: Ищет книги по названию, автору или году.

```change_book_status(self, book_id, new_status)```: Меняет статус книги (в наличии/выдана).

```display_books(self)```: Отображает все книги в библиотеке.

Основная функция **_```main```_**:
    Запускает приложение и позволяет пользователю взаимодействовать с библиотекой книг через меню.


## Структура данных
### Все книги хранятся в JSON файле. Каждая книга представляет собой объект с полями:

```id```: уникальный идентификатор книги.

```title```: название книги.

```author```: автор книги.

```year```: год издания книги.

```status```: статус книги, может быть "в наличии" или "выдана".


## Пример записи для одной книги:

```
{
    "id": 1,
    "title": "Война и мир",
    "author": "Лев Толстой",
    "year": 1869,
    "status": "в наличии"
}
```


## Пример работы программы
### Меню программы:

Меню:
1. Добавить книгу
2. Удалить книгу
3. Поиск книги
4. Отобразить все книги
5. Изменить статус книги
6. Выход


## Пример добавления книги:
```
Введите название книги: Война и мир
Введите автора книги: Лев Толстой
Введите год издания книги: 1869
Книга добавлена.
```

## Пример поиска книги:
```
Введите текст для поиска: Толстой
Найденные книги:
ID: 1
Название: Война и мир
Автор: Лев Толстой
Год издания: 1869
Статус: в наличии
```

## Пример изменения статуса книги:

```
Введите id книги для изменения статуса: 1
Введите новый статус (в наличии/выдана): выдана
Статус книги изменен на 'выдана'.
```


### **Инструкция по загрузке и установки приложения:**


| STEP | INSTRUCTION                                                                                       |
|-----:|---------------------------------------------------------------------------------------------------|
|    1 | _Клонируем репозиторий на ПК:_<br/>```git clone https://github.com/AntiViruS90/LibraryTest.git``` |
|    2 | _Переходим в репозиторий:_<br/> ```cd LibraryTest```                                              |
|    3 | _Активируем приложение:_ <br/>```python3 main.py```                                               |
