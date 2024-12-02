from library import Library
from logic import (
    repeat_enter_int_attr,
    repeat_enter_correct_status,
    repeat_not_empty_data,
)


def main():
    library = Library()

    print("\n📚 Добро пожаловать в библиотечный менеджер 📚\n")
    while True:
        print("\nВыберите действие:")
        print("1️⃣  Добавить книгу")
        print("2️⃣  Удалить книгу")
        print("3️⃣  Найти книгу")
        print("4️⃣  Посмотреть все книги")
        print("5️⃣  Изменить статус книги")
        print("6️⃣  Завершить работу и сохранить данные")
        print("0️⃣  Выход без сохранения")

        choice = input("\nВаш выбор: ").strip()
        match choice:
            case '1':
                title = repeat_not_empty_data("название")
                author = repeat_not_empty_data("автора")
                year = repeat_enter_int_attr("Введите год издания (целое число): ")
                library.add_book(title, author, int(year))

            case '2':
                book_id = repeat_enter_int_attr("Введите ID книги для удаления: ")
                library.delete_book(book_id)

            case '3':
                book_id = repeat_enter_int_attr("Введите ID книги для поиска: ")
                book = library.get_book(book_id)
                if book:
                    print("\n📖 Найденная книга:")
                    print(f"ID: {book.book_id}\nНазвание: {book.title}\nАвтор: {book.author}\nГод: {book.year}\nСтатус: {book.status}")
                else:
                    print("❌ Книга с указанным ID не найдена.")

            case '4':
                print("\n📚 Все книги в библиотеке:")
                library.get_books()

            case '5':
                book_id = repeat_enter_int_attr("Введите ID книги для изменения статуса: ")
                status = repeat_enter_correct_status()
                library.change_status_book(book_id, status)

            case '6':
                library.save_to_file('library')
                print("\n✅ Работа завершена, все данные сохранены! До свидания!\n")
                break

            case '0':
                print("\n❌ Выход без сохранения данных. До свидания!\n")
                break

            case _:
                print("\n❌ Ошибка: Некорректный выбор. Попробуйте снова.\n")


if __name__ == '__main__':
    main()
