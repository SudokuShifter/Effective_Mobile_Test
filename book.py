class Book:
    """
    Класс Book отвечает за сохранение объектов книг в контексте определённого интерфейса данного класса
    """
    def __init__(self, book_id: int, title: str, author: str, year: int):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = 'в наличии'

    def __str__(self):
        return f'Title: {self.title} - Author: {self.author} - Year: {self.year} - status: {self.status}'

    def __repr__(self):
        return f'ID: {self.id} - Title: {self.title}'