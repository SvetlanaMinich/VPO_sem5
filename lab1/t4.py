def gradient(height, start, stop):
    """
    Создает цветовой градиент от цвета start до цвета stop высотой height.
    
    Аргументы:
    height -- высота градиента (количество строк)
    start -- начальный цвет в формате RGB (кортеж из трех значений)
    stop -- конечный цвет в формате RGB (кортеж из трех значений)
    
    Возвращает:
    table -- список строк таблицы, каждая строка представляет собой градиентный цвет
    """
    table = []  # Список для хранения строк градиента
    
    # Проверка, что height — положительное целое число
    if not isinstance(height, int) or height <= 0:
        print("ОШИБКА. Высота должна быть положительным целым числом.")
        return table
    
    # Проверка, что start и stop — корректные RGB кортежи
    for color in [start, stop]:
        if len(color) != 3 or any(not isinstance(c, int) or c < 0 or c > 255 for c in color):
            print("ОШИБКА. Цвета должны быть кортежами из трёх целых чисел в диапазоне от 0 до 255.")
            return table
    
    # Основной цикл для построения градиента
    for y in range(height):
        progress = y / (height - 1)  # Прогресс от 0 до 1, где 0 — это start, 1 — это stop
        # Расчет текущего цвета по формуле линейной интерполяции
        color = tuple(int(start[i] * (1 - progress) + stop[i] * progress) for i in range(3))
        # Преобразование RGB цвета в шестнадцатеричный формат
        color = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])
        # Добавляем строку с ячейкой определенного цвета в таблицу
        table.append(f'<td style="background-color: {color.upper()}; width:500px; height:2px;"></td>')
    
    return table  # Возвращаем список строк таблицы


# # Создаем таблицу с градиентом высотой 1024 строк, от белого до черного
# table = gradient(1024, (255, 255, 255), (0, 0, 0))

# # Формируем HTML-код для отображения таблицы
# html_table = f"""
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Color Gradient Table</title>
#     <style>
#         table {{
#             border-collapse: collapse;
#         }}
#     </style>
# </head>
# <body>
#     <table>
#         {"".join([f'<tr>{row}</tr>' for row in table])}
#     </table>
# </body>
# </html>
# """

# # Сохраняем HTML-код в файл
# with open("color_gradient_table.html", "w", encoding="utf-8") as file:
#     file.write(html_table)


import unittest
from unittest.mock import patch

# Класс с тестами для функции gradient
class TestGradient(unittest.TestCase):

    @patch('builtins.print')
    def test_gradient_valid(self, mock_print):
        """Тестирует корректное создание градиента с правильными входными данными."""
        result = gradient(3, (255, 0, 0), (0, 0, 255))  # Градиент от красного до синего
        
        expected = [
            '<td style="background-color: #FF0000; width:500px; height:2px;"></td>',
            '<td style="background-color: #7F007F; width:500px; height:2px;"></td>',
            '<td style="background-color: #0000FF; width:500px; height:2px;"></td>'
        ]
        
        self.assertEqual(result, expected)
        mock_print.assert_not_called()  # Убедиться, что ошибок не было

    @patch('builtins.print')
    def test_gradient_invalid_height(self, mock_print):
        """Тестирует случай с некорректной высотой градиента."""
        result = gradient(-5, (255, 0, 0), (0, 0, 255))
        
        expected = []
        self.assertEqual(result, expected)
        mock_print.assert_called_with("ОШИБКА. Высота должна быть положительным целым числом.")

    @patch('builtins.print')
    def test_gradient_invalid_color(self, mock_print):
        """Тестирует случай с некорректными цветами."""
        result = gradient(3, (255, 0, 0), (256, 0, 0))
        
        expected = []
        self.assertEqual(result, expected)
        mock_print.assert_called_with("ОШИБКА. Цвета должны быть кортежами из трёх целых чисел в диапазоне от 0 до 255.")

    @patch('builtins.print')
    def test_gradient_invalid_color_length(self, mock_print):
        """Тестирует случай с некорректной длиной цветового кортежа."""
        result = gradient(3, (255, 0, 0, 0), (0, 0, 255))
        
        expected = []
        self.assertEqual(result, expected)
        mock_print.assert_called_with("ОШИБКА. Цвета должны быть кортежами из трёх целых чисел в диапазоне от 0 до 255.")

    @patch('builtins.print')
    def test_gradient_invalid_color_type(self, mock_print):
        """Тестирует случай с некорректным типом цвета (не числа)."""
        result = gradient(3, ('255', 0, 0), (0, 0, 255))
        
        expected = []
        self.assertEqual(result, expected)
        mock_print.assert_called_with("ОШИБКА. Цвета должны быть кортежами из трёх целых чисел в диапазоне от 0 до 255.")

# Запуск тестов
if __name__ == '__main__':
    unittest.main()