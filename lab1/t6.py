import requests
from urllib.parse import urlparse
import os

def task6(url: str, save_dir_path: str):
    """
    Функция для скачивания файла с указанного URL и сохранения его в указанную директорию.

    Аргументы:
    url -- URL для скачивания файла.
    save_dir_path -- Путь к папке, в которой будет сохранён файл.
    """

    # Проверяем корректность URL, разбирая его на компоненты
    try:
        parse_res = urlparse(url=url)  # Разбираем URL на компоненты
        if not parse_res.scheme or not parse_res.netloc:  # Проверяем наличие схемы (http/https) и хоста
            print("ОШИБКА. Некорректный URL.")
            return
    except Exception:
        print(f"ОШИБКА. Невозможно обработать URL.")
        return

    # Проверяем, существует ли указанная папка для сохранения файла
    if not os.path.isdir(save_dir_path):  # Проверяем, что директория существует
        print(f"ОШИБКА. Указанная папка '{save_dir_path}' не существует.")
        return

    # Извлекаем имя файла из URL
    file_name = os.path.basename(parse_res.path)  # Извлекаем имя файла из пути в URL
    if not file_name:  # Если не удается извлечь имя файла, выводим ошибку
        print("ОШИБКА. Невозможно извлечь имя файла из URL.")
        return

    # Формируем полный путь для сохранения файла
    file_path = os.path.join(save_dir_path, file_name)  # Полный путь для сохранения файла

    # Попытка загрузки файла с URL
    try:
        # Скачиваем файл по частям, чтобы не загружать его целиком в память
        response = requests.get(url, stream=True)  # Запрос на загрузку файла с URL
        response.raise_for_status()  # Проверяем статус ответа. Если ошибка, вызываем исключение
    except Exception:
        print(f"ОШИБКА. Не удалось скачать файл.")  # Если возникла ошибка при загрузке, выводим сообщение
        return

    # Сохранение файла на локальный диск
    try:
        with open(file_path, 'wb') as file:  # Открываем файл для записи в бинарном режиме
            for chunk in response.iter_content(chunk_size=8192):  # Загружаем файл по частям (8КБ за раз)
                file.write(chunk)  # Записываем каждую часть в файл
        print(f"Файл успешно сохранён в: {file_path}")  # Сообщение о успешном сохранении файла
    except Exception:
        print(f"ОШИБКА. Не удалось сохранить файл.")  # Если не удалось сохранить файл, выводим сообщение об ошибке
        return


task6('https://filesampleshub.com/download/document/txt/sample1.txt', 
      r'C:\sem5\vpo\lab1\t5_dir')