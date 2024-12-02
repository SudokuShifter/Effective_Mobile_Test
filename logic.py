def repeat_enter_int_attr(description: str):
    """
    Метод repeat_enter_int_attr упрощает процесс ввода числовых
    данных путём бесконечного цикла до момента передачи корректных данных
    """
    while True:
        some_attr = input(description)
        if some_attr.isdigit():
            return int(some_attr)


def repeat_enter_correct_status():
    """
    Метод repeat_enter_correct_status упррщает процесс ввода статуса книги
    путём бесконечного цикла до момента передачи корректных данных
    """
    accept_status = ('в наличии', 'выдана')
    while True:
        status = input('Введите статус, который хотите установить: \n')
        if status.lower() in accept_status:
            return status
        print(f"❌ Ошибка: Некорректный статус. Допустимые значения: {accept_status}.")


def repeat_not_empty_data(description: str):
    while True:
        data = input(f'Введите {description} книги: ')
        if len(data) > 0:
            return data