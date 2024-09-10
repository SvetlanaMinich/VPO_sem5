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
    
    # Проверка, что start и stop — корректные RGB кортежи
    for color in [start, stop]:
        if len(color) != 3 or any(not isinstance(c, int) or c < 0 or c > 255 for c in color):
            print("ОШИБКА. Цвета должны быть кортежами из трёх целых чисел в диапазоне от 0 до 255.")
    
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


# Создаем таблицу с градиентом высотой 1024 строк, от белого до черного
table = gradient(1024, (255, 255, 255), (0, 0, 0))

# Формируем HTML-код для отображения таблицы
html_table = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Color Gradient Table</title>
    <style>
        table {{
            border-collapse: collapse;
        }}
    </style>
</head>
<body>
    <table>
        {"".join([f'<tr>{row}</tr>' for row in table])}
    </table>
</body>
</html>
"""

# Сохраняем HTML-код в файл
with open("color_gradient_table.html", "w", encoding="utf-8") as file:
    file.write(html_table)
