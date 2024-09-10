def task3():
    # Ввод значения переменной a
    a = input('Введите положительное число a: ')
    
    # Проверка и преобразование a в число (вещественное или целое) с обработкой исключений
    try:
        a = float(a)  # Преобразуем ввод в вещественное число
        if a <= 0:  # Проверка, что a — положительное число
            print('ОШИБКА. Число a должно быть положительным.')
            return  # Прерываем выполнение функции
    except ValueError:
        print('ОШИБКА. Значение a должно быть числом (целым или вещественным).')
        return  # Прерываем выполнение функции
    
    # Ввод значения переменной b
    b = input('Введите положительное число b: ')
    
    # Проверка и преобразование b в число (вещественное или целое) с обработкой исключений
    try:
        b = float(b)  # Преобразуем ввод в вещественное число
        if b <= 0:  # Проверка, что b — положительное число
            print('ОШИБКА. Число b должно быть положительным.')
            return  # Прерываем выполнение функции
    except ValueError:
        print('ОШИБКА. Значение b должно быть числом (целым или вещественным).')
        return  # Прерываем выполнение функции
    
    # Вывод произведения чисел a и b (площади прямоугольника)
    print(f"Площадь прямоугольника: {a} * {b} = {a * b}")  # Форматированный вывод результата



import unittest
from unittest.mock import patch

# Класс с тестами для функции task3
class TestTask3(unittest.TestCase):

    # Тест с корректным вводом положительных чисел
    @patch('builtins.input', side_effect=['5', '10'])  # Подмена ввода для a и b
    @patch('builtins.print')  # Подмена функции print
    def test_task3_valid_input(self, mock_print, mock_input):
        task3()  # Вызов функции task3

        # Ожидаемый результат (площадь прямоугольника)
        expected_calls = [
            unittest.mock.call('Площадь прямоугольника: 5.0 * 10.0 = 50.0')
        ]
        mock_print.assert_has_calls(expected_calls)  # Проверка, что print был вызван с правильными аргументами

    # Тест с некорректным вводом a (нечисловое значение)
    @patch('builtins.input', side_effect=['abc', '10'])  # Подмена ввода, где a - не число
    @patch('builtins.print')  # Подмена функции print
    def test_task3_invalid_input_a(self, mock_print, mock_input):
        task3()  # Вызов функции task3

        # Ожидаемый вывод об ошибке для a
        expected_calls = [
            unittest.mock.call('ОШИБКА. Значение a должно быть числом (целым или вещественным).')
        ]
        mock_print.assert_has_calls(expected_calls)  # Проверка вывода ошибки

    # Тест с некорректным вводом b (нечисловое значение)
    @patch('builtins.input', side_effect=['5', 'xyz'])  # Подмена ввода, где b - не число
    @patch('builtins.print')  # Подмена функции print
    def test_task3_invalid_input_b(self, mock_print, mock_input):
        task3()  # Вызов функции task3

        # Ожидаемый вывод об ошибке для b
        expected_calls = [
            unittest.mock.call('ОШИБКА. Значение b должно быть числом (целым или вещественным).')
        ]
        mock_print.assert_has_calls(expected_calls)  # Проверка вывода ошибки

    # Тест с отрицательным значением a
    @patch('builtins.input', side_effect=['-5', '10'])  # Подмена ввода, где a - отрицательное число
    @patch('builtins.print')  # Подмена функции print
    def test_task3_negative_a(self, mock_print, mock_input):
        task3()  # Вызов функции task3

        # Ожидаемый вывод об ошибке для a
        expected_calls = [
            unittest.mock.call('ОШИБКА. Число a должно быть положительным.')
        ]
        mock_print.assert_has_calls(expected_calls)  # Проверка вывода ошибки

    # Тест с отрицательным значением b
    @patch('builtins.input', side_effect=['5', '-10'])  # Подмена ввода, где b - отрицательное число
    @patch('builtins.print')  # Подмена функции print
    def test_task3_negative_b(self, mock_print, mock_input):
        task3()  # Вызов функции task3

        # Ожидаемый вывод об ошибке для b
        expected_calls = [
            unittest.mock.call('ОШИБКА. Число b должно быть положительным.')
        ]
        mock_print.assert_has_calls(expected_calls)  # Проверка вывода ошибки

    # Тест с вводом нуля для a
    @patch('builtins.input', side_effect=['0', '10'])  # Подмена ввода, где a - 0
    @patch('builtins.print')  # Подмена функции print
    def test_task3_zero_a(self, mock_print, mock_input):
        task3()  # Вызов функции task3

        # Ожидаемый вывод об ошибке для a
        expected_calls = [
            unittest.mock.call('ОШИБКА. Число a должно быть положительным.')
        ]
        mock_print.assert_has_calls(expected_calls)  # Проверка вывода ошибки

    # Тест с вводом нуля для b
    @patch('builtins.input', side_effect=['10', '0'])  # Подмена ввода, где b - 0
    @patch('builtins.print')  # Подмена функции print
    def test_task3_zero_b(self, mock_print, mock_input):
        task3()  # Вызов функции task3

        # Ожидаемый вывод об ошибке для b
        expected_calls = [
            unittest.mock.call('ОШИБКА. Число b должно быть положительным.')
        ]
        mock_print.assert_has_calls(expected_calls)  # Проверка вывода ошибки


# Запуск тестов
if __name__ == '__main__':
    unittest.main()
