import os
import json
from typing import List


class Book:
    def __init__(self, id: int, title: str, author: str, year: int, status: str):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status
        
        
    def __str__(self):
        return (f"id: {self.id},"
                f"Название: {self.title}, "
                f"Автор: {self.author}, "
                f"Год издания: {self.year}, "
                f"Статус: {self.status}" )
        

class Library:
    LIB_FILE = "library.json"
    
    def __init__(self):
        self.books = []
        self.LIB_FILE = "library.json"
        self.file_books()


# ЗАГРУЗКА СУЩЕСТВУЮЩЕЙ БИБЛИОТЕКИ / ПРОВЕРКА JSON

    def file_books(self) -> List[Book]:
        if os.path.exists(self.LIB_FILE):
            try: 
                with open(self.LIB_FILE, "r", encoding='utf-8') as file:
                    books_data = json.load(file)
                    self.books = [Book(**book) for book in books_data]
            except json.JSONDecodeError:
                print('\nОшибка чтения. Перезапись!\n')
        else:
            print("Файл отсутвует, создаю новый")


# ЗАПИСЬ (ДОБАВЛЕНИЕ) КНИГ

    def save_books(self):
        with open(self.LIB_FILE, "w", encoding="utf-8") as file:
            books_data = [book.__dict__ for book in self.books]
            json.dump(books_data, file, indent=4, ensure_ascii=False)
            
            
# ДОБАВЛЕНИЕ КНИГ (ВВОД ПОЛЬЗОВАТЕЛЕМ НАЗВАНИЕ | АВТОР | ГОД) id | status автоматически

    def add_book(self):
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        year = input("Введите год издания книги: ")
        status = "в наличии"

        book_id = len(self.books) + 1
        new_book = Book(book_id, title, author, int(year), status)
        self.books.append(new_book)
        self.save_books()
        print("Книга добавлена!")
    

# УДАЛЕНИЕ КНИГИ ИЗ БИБЛИОТЕКИ

    def delete_book(self):
        book_id = int(input("Введите ID книги для удаления: "))
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.save_books()
                print("Книга удалена!")
                return
        print("Книга с таким ID не найдена.")


# ПОИСК КНИГИ (НАЗВАНИЕ , АВТОР ИЛИ ГОД)

    def search_books(self):
        keyword = input("Введите ключ для поиска (название , автор или год): ").lower()
        found_books = [
            book for book in self.books
            if keyword in book.title.lower() or
            keyword in book.author.lower() or
            keyword == str(book.year)
        ]
        if found_books:
            print("Найденные книги: ")
            for book in found_books:
                print(book)
        else:
            print("Книг по вашему запросу не найдено.")


# ПОКАЗ ВСЕХ КНИГ

    def display_books(self):
        if not self.books:
            print("Библиотека пуста.")
        else:
            print("Список книг:")
            for book in self.books:
                print(book)


# СМЕНА СТАТУСА (В НАЛИЧИИ / ВЫДАНА)

    def change_status(self):
        book_id = int(input("Введите ID книги: "))
        for book in self.books:
            if book.id == book_id:
                new_status = input("Введите новый статус ('в наличии' или 'выдана'): ")
                if new_status in ["в наличии", "выдана"]:
                    book.status = new_status
                    self.save_books()
                    print("Статус обновлён!")
                else:
                    print("Неверный статус.")
                return
        print("Книга с таким ID не найдена.")


# МЕНЮ ДЛЯ ПОЛЬЗОВАТЕЛЯ

def main():
    library = Library()
    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("0. Выйти\n")

        choice = input("Выберите действие: ")
        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.delete_book()
        elif choice == "3":
            library.search_books()
        elif choice == "4":
            library.display_books()
        elif choice == "5":
            library.change_status()
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте ещё раз.")


if __name__ == "__main__":
    main()