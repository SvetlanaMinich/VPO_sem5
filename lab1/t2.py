def task2():
    # Создаем пустой список для хранения данных о людях
    people = []
    
    # Бесконечный цикл для ввода данных о каждом человеке
    while True:
        # Ввод имени с проверкой на пустую строку и соответствие правилам
        name = input('Введите Имя с заглавной буквы или нажмите <Enter> чтобы закончить: ')
        if name == '':  # Если пользователь нажал Enter, завершаем ввод
            break
        if name[0].lower() == name[0]:  # Проверяем, начинается ли имя с заглавной буквы
            print('ОШИБКА. Имя должно начинаться с большой буквы.')
            return
        
        # Проверяем, есть ли в имени цифры и специальные символы
        for i in name:
            if not i.isalpha():  # Если найдена цифра в имени
                print('ОШИБКА. Имя должно содержать только буквы.')
                return   

        # Ввод фамилии с проверкой на пустую строку и соответствие правилам
        surname = input('Введите Фамилию с заглавной буквы: ')
        if surname[0].lower() == surname[0]:  # Проверяем, начинается ли фамилия с заглавной буквы
            print("ОШИБКА. Фамилия должна начинаться с большой буквы.")
            return
        
        # Проверяем, есть ли в фамилии цифры
        for i in surname:
            if not i.isalpha():  # Если найдена цифра в фамилии
                print('ОШИБКА. Фамилия должна содержать только буквы.')
                return

        # Ввод возраста с проверкой на корректность
        age = input('Введите возраст: ')
        try:
            age = int(age)  # Преобразуем введённый возраст в целое число
            if age <= 0:  # Проверяем, что возраст положительный
                print(f"ОШИБКА. Возраст должен быть положительным числом.")
                return
        except Exception:  # Обрабатываем исключение, если возраст не является числом
            print(f"ОШИБКА. Возраст должен быть целым числом.")
            return
            
        # Добавляем данные о человеке в список в виде словаря
        people.append({'name': name, 'surname': surname, 'age': age})
    
    # Проверка, что список людей не пустой
    if not people:  # Если список пустой, выводим сообщение
        print("Список людей пуст.")
        return

    # Цикл для вывода данных о каждом человеке
    for person in people:  # Перебираем каждого человека в списке
        print(f"{person['surname']} {person['name']} {person['age']}")  # Выводим фамилию, имя и возраст
    
    # Создаем список возрастов всех людей
    ages = [i['age'] for i in people]  # Извлекаем возраст каждого человека в отдельный список
    
    # Находим минимальный, максимальный возраст и средний возраст
    min_age, max_age, avr_age = min(ages), max(ages), round(sum(ages) / len(ages), 2)
    
    # Выводим минимальный, максимальный и средний возраст
    print(f"Минимальный возраст: {min_age}, Максимальный возраст: {max_age}, Средний возраст: {avr_age}")



import unittest
from unittest.mock import patch

# Класс с тестами для функции task2
class TestTask2(unittest.TestCase):
    
    # Тест с вводом данных для одного человека
    @patch('builtins.input', side_effect=['John', 'Doe', '30', ''])  # Подмена ввода с фиктивными данными
    @patch('builtins.print')  # Подмена функции print
    def test_task2_single_person(self, mock_print, mock_input):
        task2()  # Вызов функции task2
        
        # Ожидаемый результат для одного человека
        expected_calls = [
            unittest.mock.call('Doe John 30'),
            unittest.mock.call('Минимальный возраст: 30, Максимальный возраст: 30, Средний возраст: 30.0')
        ]
        mock_print.assert_has_calls(expected_calls)  # Проверка, что print вызвался с ожидаемыми аргументами

    
    # Тест с вводом данных для двух человек
    @patch('builtins.input', side_effect=['Jane', 'Doe', '25', 'John', 'Smith', '40', ''])  # Подмена ввода для двух человек
    @patch('builtins.print')  # Подмена функции print
    def test_task2_multiple_people(self, mock_print, mock_input):
        task2()  # Вызов функции task2
        
        # Ожидаемый результат для двух человек
        expected_calls = [
            unittest.mock.call('Doe Jane 25'),
            unittest.mock.call('Smith John 40'),
            unittest.mock.call('Минимальный возраст: 25, Максимальный возраст: 40, Средний возраст: 32.5')
        ]
        mock_print.assert_has_calls(expected_calls)  # Проверка, что print вызвался с ожидаемыми аргументами

    
    # Тест с пустым вводом (нажатие Enter без данных)
    @patch('builtins.input', side_effect=[''])  # Подмена ввода: пользователь нажимает только Enter
    @patch('builtins.print')  # Подмена функции print
    def test_task2_empty_input(self, mock_print, mock_input):
        task2()  # Вызов функции task2
        
        # Ожидаемый результат: список пуст
        expected_calls = [
            unittest.mock.call('Список людей пуст.')
        ]
        mock_print.assert_has_calls(expected_calls)  # Проверка вывода сообщения о пустом списке

    
    # Тест с ошибкой, когда имя начинается с маленькой буквы
    @patch('builtins.input', side_effect=['john', 'Doe', '30', ''])  # Подмена ввода для проверки на маленькую букву
    @patch('builtins.print')  # Подмена функции print
    def test_task2_invalid_name_lowercase(self, mock_print, mock_input):
        task2()  # Вызов функции task2
        
        # Ожидаемый вывод об ошибке
        expected_calls = [
            unittest.mock.call('ОШИБКА. Имя должно начинаться с большой буквы.')
        ]
        mock_print.assert_has_calls(expected_calls)  # Проверка вывода ошибки

    
    # Тест с ошибкой, когда имя содержит цифры
    @patch('builtins.input', side_effect=['John1', 'Doe', '30', ''])  # Подмена ввода для проверки на цифры в имени
    @patch('builtins.print')  # Подмена функции print
    def test_task2_invalid_name_with_digits(self, mock_print, mock_input):
        task2()  # Вызов функции task2
        
        # Ожидаемый вывод об ошибке
        expected_calls = [
            unittest.mock.call('ОШИБКА. Имя не должно содержать цифр.')
        ]
        mock_print.assert_has_calls(expected_calls)  # Проверка вывода ошибки

    
    # Тест с ошибкой, когда фамилия пустая
    @patch('builtins.input', side_effect=['John', '', ''])  # Подмена ввода для проверки на пустую фамилию
    @patch('builtins.print')  # Подмена функции print
    def test_task2_empty_surname(self, mock_print, mock_input):
        task2()  # Вызов функции task2
        
        # Ожидаемый вывод об ошибке
        expected_calls = [
            unittest.mock.call('ОШИБКА. Фамилия не может быть пустой.')
        ]
        mock_print.assert_has_calls(expected_calls)  # Проверка вывода ошибки

    
    # Тест с ошибкой, когда фамилия начинается с маленькой буквы
    @patch('builtins.input', side_effect=['John', 'doe', '30', ''])  # Подмена ввода для проверки на маленькую букву в фамилии
    @patch('builtins.print')  # Подмена функции print
    def test_task2_invalid_surname_lowercase(self, mock_print, mock_input):
        task2()  # Вызов функции task2
        
        # Ожидаемый вывод об ошибке
        expected_calls = [
            unittest.mock.call('ОШИБКА. Фамилия должна начинаться с большой буквы.')
        ]
        mock_print.assert_has_calls(expected_calls)  # Проверка вывода ошибки

    
    # Тест с ошибкой, когда фамилия содержит цифры
    @patch('builtins.input', side_effect=['John', 'Doe1', '30', ''])  # Подмена ввода для проверки на цифры в фамилии
    @patch('builtins.print')  # Подмена функции print
    def test_task2_invalid_surname_with_digits(self, mock_print, mock_input):
        task2()  # Вызов функции task2
        
        # Ожидаемый вывод об ошибке
        expected_calls = [
            unittest.mock.call('ОШИБКА. Фамилия не должна содержать цифр.')
        ]
        mock_print.assert_has_calls(expected_calls)  # Проверка вывода ошибки

    
    # Тест с ошибкой, когда возраст отрицательный
    @patch('builtins.input', side_effect=['John', 'Doe', '-5', ''])  # Подмена ввода для проверки на отрицательный возраст
    @patch('builtins.print')  # Подмена функции print
    def test_task2_invalid_age_negative(self, mock_print, mock_input):
        task2()  # Вызов функции task2
        
        # Ожидаемый вывод об ошибке
        expected_calls = [
            unittest.mock.call('ОШИБКА. Возраст должен быть положительным числом.')
        ]
        mock_print.assert_has_calls(expected_calls)  # Проверка вывода ошибки

    
    # Тест с ошибкой, когда возраст не является числом
    @patch('builtins.input', side_effect=['John', 'Doe', 'abc', ''])  # Подмена ввода для проверки на нечисловой возраст
    @patch('builtins.print')  # Подмена функции print
    def test_task2_invalid_age_non_numeric(self, mock_print, mock_input):
        task2()  # Вызов функции task2
        
        # Ожидаемый вывод об ошибке
        expected_calls = [
            unittest.mock.call('ОШИБКА. Возраст должен быть числом.')
        ]
        mock_print.assert_has_calls(expected_calls)  # Проверка вывода ошибки


# Запуск тестов
if __name__ == '__main__':
    task2()
