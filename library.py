import json

from book import Book


class Library:
    """
    Класс Library отвечает за временное хранилище книг с последующим переносом в json-файл при окончании работы.
    В классе реализованы основные операции над книгами, такие как: добавление, удаление, изменение статуса, получение
    """

    def __init__(self):
        """
        Магический метод __init__ хранит в себе временные данные о добавленных книгах.
        При окончании работы в dump будут переданы данные отсюда.
        Так же тут реализован метод формирования id книги, чтобы он генерировался автоматически при её создании.
        """
        self.books = [] if not Library.load_from_file('library') \
            else Library.load_from_file('library')
        self.next_book_id = 0 if not self.books else self.books[-1].book_id + 1


    def add_book(self, title: str, author: str, year: int):
        """
        Метод add_book отвечает за добавление книги.
        Принимает следующие параметры: title, author, year.
        Внутри себя валидирует поступающие данные и создаёт книгу,
        либо выводит предупреждение о некорректных данных.
        """
        if not self.check_unique_title(title):

            if 0 < year <= 2024:
                book_for_append = Book(self.next_book_id, title, author, year)
                self.books.append(book_for_append)
                self.next_book_id += 1
                print(f"{'*' * 20}\n✅ Книга добавлена успешно!\n"
                      f"Название: {title}\nАвтор: {author}\nГод издания: {year}\n{'*' * 20}")

            else:
                print(f"❌ Ошибка: Год указан некорректно (должен быть от 0 до 2024).")

        else:
            print(f"❌ Ошибка: Книга с названием \"{title}\" уже существует. "
                f"Пожалуйста, используйте уникальное название.")


    def delete_book(self, book_id: int):
        """
        Метод delete_book удаляет книгу по переданному id.
        Если id существует, то книга будет удалена.
        Если нет, то будет выведено предупреждение
        """
        book = self.get_book(book_id)

        if book:
            self.books.remove(book)
            print(f"{'*' * 20}\n🗑️ Книга с ID {book_id} удалена успешно!\n{'*' * 20}")

        else:
            print(f"❌ Ошибка: Книга с ID {book_id} не найдена. Проверьте идентификатор и повторите попытку.")


    def get_book(self, book_id: int):
        """
        Метод get_book позволяет получить книгу по переданному id.
        Если книга существует, возвращает книгу.
        Если нет, возвращает None
        """
        if self.books:
            return next((book for book in self.books if book.book_id == book_id), None)


    def get_books(self):
        """
        Метод get_books позволяет получить все существующие книги.
        Если книги существуют, возвращает книги.
        Если нет, выводит предупреждение
        """
        if not self.books:
            print(f"{'*' * 20}\n📚 Библиотека пуста.\n{'*' * 20}")

        else:
            print(f"{'*' * 20}\n📚 Все книги в библиотеке:\n")

            for book in self.books:
                print(
                    f"ID: {book.book_id}\nНазвание: {book.title}\nАвтор: {book.author}\nГод: {book.year}\nСтатус: {book.status}\n{'-' * 20}")
            print(f"{'*' * 20}")


    def change_status_book(self, book_id: int, status: str):
        """
        Метод change_status_book позволяет сменить статус книги.
        Валидация поступающих данных проводится в entrypoint
        """
        book = self.get_book(book_id)

        if book:
            book.status = status
            print(f"✅ Статус книги с ID {book_id} успешно изменён на \"{status}\".")

        else:
            print(f"❌ Ошибка: Книга с ID {book_id} не найдена. Проверьте идентификатор и повторите попытку.")


    def check_unique_title(self, title: str):
        """
        Метод check_unique_title проверяет уникальность переданного названия книги.
        Если название уникально, то возвращает None.
        Если нет, возвращает существующую книгу
        """
        if self.books:
            return next((book for book in self.books if book.title == title), None)


    def save_to_file(self, filename: str):
        """
        Метод save_to_file сохраняет текущий список книг в json-файл
        """
        with open(f'{filename}.json', 'w', encoding='utf-8') as file:
            data = [book.__dict__ for book in self.books]
            json.dump(data, file, ensure_ascii=False)

        print(f"{'*' * 20}\n💾 Данные библиотеки успешно сохранены в файл \"{filename}.json\".\n{'*' * 20}")


    @staticmethod
    def load_from_file(filename: str):
        """
        Метод load_from_file позволяет выгрузить из json-файла существующие книги, если они есть и передать их
        в хранилище класса для взаимодействия через рабочий интерфейс в entrypoint.
        """
        try:
            with open(f'{filename}.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                print(f"{'*' * 20}\n📂 Данные библиотеки успешно загружены из файла \"{filename}.json\".\n{'*' * 20}")

                data_with_orm = [
                    Book(
                        book_id=book['book_id'],
                        title=book['title'],
                        author=book['author'],
                        year=book['year']
                    ) for book in data]

                return data_with_orm

        except FileNotFoundError:
            print(f"❌ Ошибка: Файл \"{filename}.json\" не найден. Создаётся новая библиотека.")

        except json.decoder.JSONDecodeError:
            print(f"❌ Ошибка: Не удалось загрузить данные из файла \"{filename}.json\". Проверьте его содержимое.")
