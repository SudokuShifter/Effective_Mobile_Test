import unittest
from library import Library
from book import Book


class TestLibrary(unittest.TestCase):

    def setUp(self):
        """
        Инициализация данных перед каждым тестом.
        """
        self.library = Library()

    def test_add_book(self):
        """Тест добавления книги."""
        self.library.add_book("Название книги", "Автор", 2023)
        books = self.library.books
        self.assertEqual(books[-1].title, "Название книги")
        self.assertEqual(books[-1].author, "Автор")
        self.assertEqual(books[-1].year, 2023)

    def test_delete_book(self):
        """
        Тест удаления книги.
        """
        self.library.add_book("Книга для удаления", "Автор", 2022)
        book_id = self.library.books[-1].book_id
        self.library.delete_book(book_id)
        books = self.library.books
        self.assertEqual(len(books), len(self.library.books))

    def test_get_book(self):
        """
        Тест получения книги по ID
        ."""
        self.library.add_book("Найти книгу", "Автор", 2021)
        book = self.library.books[-1]
        self.assertIsNotNone(book)
        self.assertEqual(book.title, "Найти книгу")

    def test_change_status_book(self):
        """
        Тест изменения статуса книги.
        """
        self.library.add_book("Книга для теста", "Автор", 2020)
        book_id = self.library.books[-1].book_id
        self.library.change_status_book(book_id, "выдана")
        book = self.library.get_book(book_id)
        self.assertEqual(book.status, "выдана")

    def test_unique_title(self):
        """
        Тест проверки уникальности названия.
        """
        self.library.add_book("Уникальное название", "Автор", 2022)
        self.assertEqual(self.library.check_unique_title('Уникальное название').title, self.library.books[-1].title)

